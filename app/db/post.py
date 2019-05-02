from ..libs.error import Error
from .models.post import PostModel
from .models.category import CategoryModel
from .models.tag import TagModel

class Post:
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
    
    def getPosts(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise Error(u'limit必须大于0且小于等于50', 400, 
                        msg_en='limit must between 0 and 50')
