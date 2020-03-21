from server.dao.post import Post
from server.dao.category import Category
from server.dao.tag import Tag
from server.dao.post_tag import PostTag


def insertCategory(category_name):
    category_query = Category.queryByCategoryName(category_name)
    return (
        category_query.id 
        if category_query is not None else Category.insert(category_name=category_name).id
    )
def insertTag(tag_name):
    tag_query = Tag.queryByTagName(tag_name)
    return tag_query if tag_query is not None else Tag.insert(tag_name=tag_name)
def insertTags(tag_names):
    return [insertTag(str(tag_name)) for tag_name in tag_names]
def insertPostTag(post_id, tag_ids):
    return [
        PostTag.insert(post_id=post_id, tag_id=tag_id)
        for tag_id in tag_ids if PostTag.queryByPostIdAndTagId(post_id, tag_id) is None
    ]

def queryCategory(category_id):
    if category_id is not None:
        category_query = Category.queryById(category_id)
        return {
            'id': category_query.id,
            'name': category_query.category_name 
        }
    return None
def queryTags(tag_ids):
    return [
        { k: v for k, v in Tag.queryByTagId(tag_id).to_dict().items() } 
        for tag_id in tag_ids
    ]
def queryPostTags(post_id):
    return queryTags([post_tag.tag_id for post_tag in PostTag.queryByPostId(post_id)])
def queryPosts(posts):
    return [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'category': queryCategory(post.category_id),
            'tags': queryPostTags(post.id),
            'created_date': post.created_date.__format__('%Y-%m-%d %H:%M:%S'),
            'updated_date': post.updated_date if post.updated_date is None else post.updated_date.__format__('%Y-%m-%d %H:%M:%S'),
        } 
        for post in posts
    ]

def updateCategory(category_name):
    category_id = None
    category_query = Category.queryByCategoryName(category_name)
    if category_query is not None:
        category_id = Category.updateByCategoryId(category_query.id, category_name=category_name).id
    else:
        category_id = Category.insert(category_name=category_name).id
    return category_id
def updatePostTags(post_id, tag_names):
    old_post_tags = PostTag.queryByPostId(post_id)
    old_tag_ids = [ post_tag.tag_id for post_tag in old_post_tags ]
    new_tag_ids = [ 
        Tag.queryByTagName(tag_name).id 
        if Tag.queryByTagName(tag_name) is not None else insertTag(tag_name).id 
        for tag_name in tag_names 
    ]
    [ PostTag.deleteByPostIdAndTagId(post_id, old_tag_id) for old_tag_id in old_tag_ids if old_tag_id not in new_tag_ids ]
    [ PostTag.insert(post_id=post_id, tag_id=new_tag_id) for new_tag_id in new_tag_ids if new_tag_id not in old_tag_ids ]
def updatePost(post_id, **update_items):
    category_name = update_items.get('category_name')
    tag_names = update_items.get('tag_names')
    if category_name is not None:
        update_items.update({ 'category_id': updateCategory(category_name) })
    if tag_names is not None:
        updatePostTags(post_id, tag_names)
    update_items.update({ 'updated_date': datetime.now() })
    Post.updateById(post_id, **update_items)