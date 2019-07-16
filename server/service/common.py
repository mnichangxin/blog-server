from datetime import datetime
from ..dao.post import Post
from ..dao.category import Category
from ..dao.tag import Tag
from ..dao.post_tag import PostTag
from ..utils.exception.exception import APIException, ServerException
from ..utils.decorators.is_json import is_json
from ..utils.decorators.commit import commit

def insert_category(category_name):
    category_query = Category.queryByCategoryName(category_name)
    return (
        category_query.id 
        if category_query is not None else Category.insert(category_name=category_name).id
    )

def insert_tag(tag_name):
    tag_query = Tag.queryByTagName(tag_name)
    return tag_query.id if tag_query is not None else Tag.insert(tag_name=tag_name).id

def insert_tags(tag_names):
    return [insert_tag(str(tag_name)) for tag_name in tag_names]

def insert_post_tag(post_id, tag_ids):
    return [
        PostTag.insert(post_id=post_id, tag_id=tag_id)
        for tag_id in tag_ids if PostTag.queryByPostIdAndTagId(post_id, tag_id) is None
    ]

@commit
@is_json
def post_publish(params):
    title = params.get('title')
    content = params.get('content') or ''
    category_name = params.get('category_name')
    tag_names = params.get('tag_names') or None
    created_date = params.get('created_date') or datetime.now()
    updated_date = None

    post_id = None
    category_id = None
    tag_ids = None

    if title is None:
        raise APIException('标题不能为空', 400)
    if category_name is not None:
        category_id = insert_category(category_name)
    if (tag_names is not None):
        if (isinstance(tag_names, list) is not True):
            raise APIException('标签格式不合法', 400)
        tag_ids = insert_tags(tag_names)
    try: 
        datetime.strptime(created_date.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    except (AttributeError, ValueError):
        raise APIException('创建时间不合法', 400)
    post_id = Post.insert(
        title=title, 
        content=content, 
        category_id=category_id,
        created_date=created_date, 
        updated_date=updated_date
    ).id
    insert_post_tag(post_id, tag_ids)
    return {
        'msg': '发布成功'
    }

@is_json
def post_update(params):
    title = params.get('title')
    content = params.get('content')
    created_date = params.get('created_date')

@commit
@is_json
def post_query(params):
    page_num = params.get('page_num') or 1
    page_size = params.get('page_size') or 10
    if isinstance(page_num, int) is not True or isinstance(page_size, int) is not True:
        raise APIException('page_num 或 page_size 不合法')
    post_info = Post.query(page_num, page_size)
    return {
        'msg': '查询成功',
        'data': post_info
    }