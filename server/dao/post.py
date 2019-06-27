from ..model.common import db
from ..model.post import PostModel


class Post:
    @staticmethod
    def insert(**kwargs):
        post = PostModel(**kwargs)
        db.session.add(post)
        db.session.commit()

