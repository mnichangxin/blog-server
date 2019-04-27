from flask import Flask
from .db.models import db
from .config import config

import click

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

    from .api.hooks import hooks as api_hooks_blueprint
    app.register_blueprint(api_hooks_blueprint, url_prefix='/api/v1/hooks')

    app.app_context().push()

    from . import commands

    return app
