import json

from functools import wraps
from server.utils.exception.exception import APIException, ServerException

def json_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        json_object = None
        try:
            json_object = json.loads(json.dumps(args[0]))
        except Exception as e:
            raise APIException(u'不合法的 JSON 格式', 400)
        if json_object is not None:
            return func(*args, **kwargs)
        else:
            raise APIException(u'不合法的 JSON 格式', 400) 
    return decorator