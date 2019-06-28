from flask import jsonify
from datetime import datetime
from ...dao.post import Post
from ...utils.exception.exception import APIException, ServerException
from ...utils.decorators.is_json import is_json


@is_json
def post_publish(params):
    title = params.get('title')
    content = params.get('content') or ''
    created_date = params.get('created_date') or datetime.now()
    updated_date = None
    if title is None:
        raise APIException('参数错误', 400)
    try:
        datetime.strptime(created_date, '%Y-%m-%d %X')
    except ValueError:
        raise APIException('不合法的创建时间', 400)
    try:
        Post.insert(title=title, content=content, created_date=created_date, updated_date=updated_date)
    except Exception:
        raise ServerException('服务端错误', 500)
    return {
        'msg': '发布成功'
    }

# @is_json
# def post_update(params):
#     title = params.get('title')
#     content = params.get('content')
#     created_date = params.get('created_date')