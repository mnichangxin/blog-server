import click
import os

from app import create_app, db
from app.models import Article, Category, Tag

app = create_app()

@app.cli.command()
def init():
    try:
        db.create_all()
    except Exception as e:
        click.echo('DB init fail: ' + '\n')
        print(e)
    else:
        click.echo('DB init success!')
