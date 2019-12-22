import click

from flask import current_app
from server.model import db

@current_app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the databases.'''
    try:
        if drop:
            if click.confirm('删除数据库，确定执行此操作？', abort=True):
                db.drop_all()
                click.echo('删除数据库成功')
            else:
                click.echo('没有任何操作')
        db.create_all()
    except click.Abort:
        click.echo('没有任何操作')
    except Exception as e:
        click.echo('初始化数据库异常')
    else:
        click.echo('初始化数据库成功')
