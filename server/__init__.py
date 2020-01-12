from flask import Flask
from werkzeug.utils import import_string
from server.model import db
from server.config.common import base_config
from server.config.blueprints import blueprints

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(base_config[config_name])
    base_config[config_name].init_app(app)

    db.init_app(app)

    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp, url_prefix='/api' + bp.url_prefix)   

    app.app_context().push()

    from .utils.common import commands

    return app

app = create_app()