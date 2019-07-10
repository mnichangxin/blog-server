from ..model.common import db
from ..model.post import PostModel
from ..utils.decorators.commit import commit

class Post:
    @staticmethod
    @commit
    def insert(**kwargs):
        post = PostModel(**kwargs)
        db.session.add(post)

