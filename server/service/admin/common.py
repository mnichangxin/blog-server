from flask import jsonify
from datetime import datetime
from ...dao.post import Post
from ...dao.category import Category
from ...utils.exception.exception import APIException, ServerException
from ...utils.decorators.is_json import is_json
from ...utils.decorators.commit import commit

@commit
@is_json
def post_publish(params):
    title = params.get('title')
    content = params.get('content') or ''
    category_name = params.get('category_name')
    created_date = params.get('created_date') or datetime.now()
    updated_date = None
    if title is None:
        raise APIException('参数错误', 400)
    if category_name is not None:
        category_name_query = Category.queryByCategoryName(category_name)
        if category_name_query is not None:
            pass
        else:
            Category.insert(category_name=category_name)
    try: 
        datetime.strptime(created_date.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    except (AttributeError, ValueError):
        raise APIException('不合法的创建时间', 400)
    try:
        Post.insert(
            title=title, 
            content=content, 
            created_date=created_date, 
            updated_date=updated_date
        )
    except Exception:
        raise ServerException('服务端错误', 500)
    return {
        'msg': '发布成功'
    }

@is_json
def post_update(params):
    title = params.get('title')
    content = params.get('content')
    created_date = params.get('created_date')