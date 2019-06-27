from flask import jsonify
from datetime import datetime
from ...dao.post import Post
from ...utils.exception.exception import APIException, ServerException
from ...utils.decorators.is_json import is_json


@is_json
def post_publish(params):
    title = params.get('title')
    content = params.get('content') or ''
    created_date = params.get('created_date')
    updated_date = params.get('updated_date') or datetime.utcnow
    if title is None or created_date is None:
        raise APIException('参数错误', 400)
    try:
        Post.insert(**params)
    except Exception as e:
        raise ServerException('服务端错误', 500)
    return {
        'msg': '发布成功'
    }