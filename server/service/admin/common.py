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
    category_id = None
    category_name = params.get('category_name')
    tags = params.get('tags') or None
    created_date = params.get('created_date') or datetime.now()
    updated_date = None
    if title is None:
        raise APIException('参数错误', 400)
    if category_name is not None:
        category_query = Category.queryByCategoryName(category_name)
        if category_query is not None:
            category_id = category_query.id
        else:
            Category.insert(category_name=category_name)
            category_id = Category.queryByCategoryName(category_name).id 
    try: 
        datetime.strptime(created_date.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    except (AttributeError, ValueError):
        raise APIException('创建时间不合法', 400)
    Post.insert(
        title=title, 
        content=content, 
        category_id=category_id,
        created_date=created_date, 
        updated_date=updated_date
    )
    return {
        'msg': '发布成功'
    }

@is_json
def post_update(params):
    title = params.get('title')
    content = params.get('content')
    created_date = params.get('created_date')