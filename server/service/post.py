from datetime import datetime
from server.dao.post import Post
from server.dao.category import Category
from server.dao.tag import Tag
from server.dao.post_tag import PostTag
from server.service.common import insertCategory, insertTags, queryPosts, updatePost
from server.utils.exception.exception import APIException, ServerException
from server.utils.decorators.commit import commit


@commit
def postPublish(params):
    title = params.get('title')
    content = params.get('content') or ''
    category_name = params.get('category_name')
    tag_names = params.get('tag_names')
    created_date = datetime.now()
    updated_date = None

    post_id = None
    category_id = None
    tag_ids = []

    if title is None:
        raise APIException('title 不能为空', 400)
    if category_name is not None:
        category_id = insertCategory(category_name)
    if (tag_names is not None):
        if (isinstance(tag_names, list) is not True):
            raise APIException('tag_names 格式不合法', 400)
        tags = insertTags(tag_names)
        tag_ids = [ tag.id for tag in tags ]
    post_id = Post.insert(
        title=title, 
        content=content, 
        category_id=category_id,
        created_date=created_date, 
        updated_date=updated_date
    ).id
    insertPostTag(post_id, tag_ids)
    return {
        'msg': '发布成功'
    }

@commit
def postQuery(params):
    page_num = params.get('page_num') or 1
    page_size = params.get('page_size') or 10
    if isinstance(page_num, int) is not True or isinstance(page_size, int) is not True:
        raise APIException('page_num 或 page_size 格式不合法')
    posts = Post.query(page_num, page_size)
    posts_data = queryPosts(posts.items)
    return {
        'msg': '查询成功',
        'data': {
            'page_index': posts.page,
            'page_count': posts.pages,
            'total': posts.total,
            'data': posts_data
        }
    }

@commit
def postDelete(params):
    post_id = params.get('post_id')
    if post_id is None:
        raise APIException('post_id 不能为空', 400)
    post_query= Post.queryById(post_id)
    if post_query is None:
        return {
            'msg': 'post_id 不存在'
        }
    Post.deleteById(post_id)
    PostTag.deleteByPostId(post_id)
    if len(Post.queryByCategoryId(post_query.category_id)) < 1:
        Category.deleteById(post_query.category_id)
    return {
        'msg': '删除成功'
    }

@commit
def postUpdate(params):
    post_id = params.get('post_id')
    category_name = params.get('category_name')
    tag_names = params.get('tag_names')
    if post_id is None:
        raise APIException('post_id 不能为空', 400)
    update_items = { k: v for k, v in params.items() if k in ['title', 'content', 'category_name', 'tag_names'] }
    updatePost(post_id, **update_items) 
    return {
        'msg': '更新成功'
    }
