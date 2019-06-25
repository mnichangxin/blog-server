from flask import jsonify
from datetime import datetime
from ...dao.post import Post
from ...utils.exception.exception import APIException
from ...utils.decorators.is_json import is_json


@is_json
def post_publish(params):
    content = params.get('cotent')
    first_date = params.get('first_date')
    if content is None or first_date is None:
        raise APIException(u'参数错误', 400)
    Post.insert()