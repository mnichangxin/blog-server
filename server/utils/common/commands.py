import click

from flask import current_app
from ...model import db

@current_app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the databases.'''
    try:
        if drop:
            if click.confirm('This operation will delete the database, do you want to continue ?', abort=True):
                db.drop_all()
                click.echo('Drop tables.')
            else:
                click.echo('Nothing operation to database.')
        db.create_all()
    except click.Abort:
        click.echo('Nothing operation to database.')
    except Exception as e:
        click.echo('Initialize the databases error.')
    else:
        click.echo('Initialized database success.')
