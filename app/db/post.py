from datetime import datetime
from ..libs.error import APIException
from .models import PostModel, CategoryModel, TagModel


class Post:
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
    
    def insertPost(self):
        post = PostModel('title1', '123456', datetime.utcnow())
        

    def getPosts(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise APIException(u'limit must between 0 and 50', 400)
        return PostModel.query.all()
