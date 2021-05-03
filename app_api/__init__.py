import yaml
import logging
from logging.config import dictConfig
from flask import (
  current_app,
  Flask,
  request,
  request_started,
  request_finished,
)
from flask.cli import load_dotenv
from .cache import cache
from .apis.v1 import bp as apiv1


load_dotenv()


def create_app():
    # initialize app
    app = Flask(__name__)

    # configure app
    app.config.from_object('config.' + app.config['ENV'].title() + 'Config')

    # configure loggings
    dictConfig(yaml.safe_load(open('logging_config.yaml', 'r'))[app.config['ENV']])
    logging.getLogger('sqlalchemy').propagate = False

    # initialize db
    # db.init_app(app)

    # initialize cache
    cache.init_app(app)

    # register blueprints
    app.register_blueprint(apiv1)

    # after request global
    app.after_request(_app_after_request)

    # connect signals
    request_started.connect(_request_started_handler, app)
    request_finished.connect(_request_finished_handler, app)

    return app


def _request_started_handler(sender, **extra):
    if _is_access_log_except_path(request.path):
        return

    current_app.logger.info(f"Request started. - {request.method} {request.url}")


def _request_finished_handler(sender, response, **extra):
    if _is_access_log_except_path(request.path):
        return

    current_app.logger.info(f"Request finished with '{response.status}'. - {request.url}")


def _app_after_request(response):
    if response.content_type == 'application/json':
        response.headers['Content-Type'] = response.content_type + '; charset=UTF-8'
    if current_app.config['ENV'] == 'development':
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
    return response


def _is_access_log_except_path(path):
    paths = [
        '/api/v1/health'
    ]
    return True if path in paths else False
