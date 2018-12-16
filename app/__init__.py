from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .api import api as api_blueprint
    from .auth import auth as auth_blueprint

    return app