from functools import wraps
from ..exception.exception import APIException, ServerException

def is_json(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        