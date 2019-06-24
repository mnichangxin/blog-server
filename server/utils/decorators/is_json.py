import json

from functools import wraps
from ..exception.exception import APIException, ServerException

def is_json(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            json_object = json.loads(json.dumps(args[0]))
        except Exception as e:
            raise APIException(u'不合法的 JSON 格式', 400)
        else:
            return func(*args, **kwargs)
    return decorator