from flask import Flask
from .db import db
from .config.config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .api.blog import blog as api_blog_blueprint
    app.register_blueprint(api_blog_blueprint, url_prefix='/api/v1/blog')

    from .api.admin import admin as api_admin_blueprint
    app.register_blueprint(api_admin_blueprint, url_prefix='/api/v1/admin')

    app.app_context().push()

    from .libs import commands, error_handler

    return app

