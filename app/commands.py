import click

from flask import current_app
from .db.models import db

@current_app.cli.command()
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

