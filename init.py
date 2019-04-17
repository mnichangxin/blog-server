import click
import os

from app import create_app, db
from app.models import Article, Category, Tag

app = create_app()

@app.cli.command()
def init():
    try:
        db.create_all()
    except:
        click.echo('DB init fail..')
    else:
        click.echo('DB init success...')
