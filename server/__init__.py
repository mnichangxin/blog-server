from flask import Flask
from server.model import db
from server.config import config
from server.api import api

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    app.register_blueprint(api, url_prefix='/api')

    app.app_context().push()

    from .utils.common import commands

    return app

