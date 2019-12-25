import json

from functools import wraps
from flask import request
from server.utils.exception.exception import APIException, ServerException

def json_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        json_object = None
        try:
            json_object = json.loads(json.dumps(request.get_json()))
        except Exception as e:
            raise APIException('参数不合法：仅接受 JSON 格式', 400)
        if json_object is not None:
            return func(*args, **kwargs)
        else:
            raise APIException('参数不合法：仅接受 JSON 格式', 400) 
    return decorator