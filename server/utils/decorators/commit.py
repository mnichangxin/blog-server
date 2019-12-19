from functools import wraps
from server.model import db

def commit(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        with db.session.begin(subtransactions=True):
            return func(*args, **kwargs)
    return decorator