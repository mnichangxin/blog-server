from flask import Flask
from .model.common import db
from .config.common import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .api.common import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .api.internal.common import internal as api_internal_blueprint
    app.register_blueprint(api_internal_blueprint, url_prefix='/api/v1/internal')

    from .api.view.common import view as api_view_blueprint
    app.register_blueprint(api_view_blueprint, url_prefix='/api/v1/view')

    app.app_context().push()

    from .utils.common import commands

    return app

