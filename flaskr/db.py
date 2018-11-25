import sqllite3

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqllite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqllite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqllite3.Row
    return g.db

def close_db(e = None):
    db = g.pop('db', None)
    if db is not None:
        db.close()