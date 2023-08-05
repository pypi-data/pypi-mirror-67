# Copyright 2019 Wilhelm Putz

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from jinjamator.daemon.api.restx import api
from jinjamator.daemon.api.endpoints.environments import (
    ns as environments_namespace,
    discover_environments,
)
from jinjamator.daemon.api.endpoints.tasks import ns as tasks_namespace, discover_tasks
from jinjamator.daemon.api.endpoints.jobs import ns as jobs_namespace
from jinjamator.daemon.api.endpoints.output_plugins import (
    ns as output_plugins_namespace,
    discover_output_plugins,
)
from jinjamator.daemon.api.endpoints.upload import ns as upload_namespace
from jinjamator.daemon.webui import webui as webui_blueprint
from jinjamator.daemon.database import db


import os, sys


import logging

app = Flask(__name__, static_folder="./webui/static")
from celery import Celery
from jinjamator.external.celery.backends.database import DatabaseBackend


celery = Celery("jinjamator")
log = logging.getLogger()


def init_celery(_configuration):
    """
    Configure Celery
    """
    celery.conf.broker_url = _configuration.get("celery_broker")
    if celery.conf.broker_url == "filesystem://":
        data_folder = os.path.join(
            _configuration.get("jinjamator_user_directory"), "broker", "data"
        )
        processed_folder = os.path.join(
            _configuration.get("jinjamator_user_directory"), "broker", "processed"
        )
        os.makedirs(data_folder, exist_ok=True)
        os.makedirs(processed_folder, exist_ok=True)
        celery.conf.broker_transport_options = {
            "data_folder_in": data_folder,
            "data_folder_out": data_folder,
            "data_folder_processed": "/app/broker/processed",
        }
    celery.conf.result_backend = _configuration.get("celery_result_backend")
    celery.conf.update({"jinjamator_private_configuration": _configuration})
    backend = DatabaseBackend(app=celery, url=app.config["CELERY_RESULT_BACKEND"])
    celery.backend = backend
    return celery


def configure(flask_app, _configuration):
    """
    Configure FLASK
    """

    flask_app.url_map.strict_slashes = False
    flask_app.config["SERVER_NAME"] = "localhost:5000"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
    flask_app.config["RESTPLUS_VALIDATE"] = True
    flask_app.config["RESTPLUS_MASK_SWAGGER"] = False
    flask_app.config["ERROR_404_HELP"] = False
    flask_app.config["CELERY_BROKER_URL"] = _configuration.get("celery_broker")
    flask_app.config["CELERY_RESULT_BACKEND"] = _configuration.get(
        "celery_result_backend"
    )
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = _configuration.get(
        "celery_result_backend"
    )
    flask_app.config["JINJAMATOR_BASE_DIRECTORY"] = _configuration.get(
        "jinjamator_base_directory"
    )
    flask_app.config["UPLOAD_FOLDER"] = "/tmp"
    flask_app.config["JINJAMATOR_GLOBAL_DEFAULTS"] = _configuration.get(
        "global_defaults"
    )
    flask_app.config["JINJAMATOR_TASKS_BASE_DIRECTORIES"] = _configuration.get(
        "global_tasks_base_dirs"
    )
    flask_app.config["JINJAMATOR_ENVIRONMENTS_BASE_DIRECTORIES"] = _configuration.get(
        "global_environments_base_dirs"
    )
    flask_app.config["JINJAMATOR_OUTPUT_PLUGINS_BASE_DIRS"] = _configuration.get(
        "global_output_plugins_base_dirs"
    )
    flask_app.config["JINJAMATOR_CONTENT_PLUGINS_BASE_DIRS"] = _configuration.get(
        "global_content_plugins_base_dirs"
    )
    flask_app.config["JINJAMATOR_FULL_CONFIGURATION"] = _configuration


def initialize(flask_app, cfg):
    """
    Initialize Jinjamator Daemon Mode
    """
    configure(flask_app, cfg)
    init_celery(cfg)

    api_blueprint = Blueprint("api", __name__, url_prefix="/api/")

    api.init_app(api_blueprint)
    api.add_namespace(environments_namespace)
    api.add_namespace(output_plugins_namespace)
    api.add_namespace(tasks_namespace)
    api.add_namespace(jobs_namespace)
    api.add_namespace(upload_namespace)
    flask_app.register_blueprint(api_blueprint)
    flask_app.register_blueprint(webui_blueprint)
    db.init_app(flask_app)


def run(cfg):
    initialize(app, cfg)
    discover_output_plugins(app)
    discover_environments(app)
    discover_tasks(app)
    port = cfg.get("daemon_listen_port", "5000")
    host = cfg.get("daemon_listen_address", "127.0.0.1")

    if "WERKZEUG_RUN_MAIN" not in os.environ.keys():
        if not cfg.get("no_worker"):
            pid = os.fork()
            if pid == 0:
                from celery import Celery

                queue = Celery("jinjamator", broker=cfg["celery_broker"])

                queue.start(
                    argv=[
                        "celery",
                        "worker",
                        "-A",
                        "jinjamator.task.celery",
                        "-c",
                        cfg.get("max_celery_worker", "2"),
                        "--max-tasks-per-child",
                        "1",
                        "-b",
                        cfg["celery_broker"],
                        "-B",
                        "-s",
                        cfg["celery_beat_database"],
                    ]
                )
                sys.exit(0)
            else:
                if not cfg.get("just_worker"):
                    log.info(f">>>>> Starting daemon at http://{host}:{port}// <<<<<")
                    app.run(
                        debug=True,
                        host=cfg.get("daemon_listen_address", "127.0.0.1"),
                        port=cfg.get("daemon_listen_port", "5000"),
                    )
                os.waitpid(pid, 0)
        else:
            log.info(f">>>>> Starting daemon at http://{host}:{port}// <<<<<")
            app.run(
                debug=True,
                host=cfg.get("daemon_listen_address", "127.0.0.1"),
                port=cfg.get("daemon_listen_port", "5000"),
            )
    else:
        log.info(f">>>>> Restarting daemon at http://{host}:{port}/ <<<<<")
        app.run(debug=True, host=host, port=port)
