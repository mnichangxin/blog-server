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

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        '''Initialize the databases.'''
        try:
            if drop:
                click.confirm('This operation will delete the database, do you want to continue ?', abort=True)
                db.drop_all()
                click.echo('Drop tables.')
            db.create_all()
        except Exception as e:
            click.echo('Initialize error: ' + '\n' + e)
        else:
            click.echo('Initialized database.')

    return app
