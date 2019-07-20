from ..model.common import db
from ..model.tb_post import PostModel

class Post:
    @staticmethod
    def insert(**kwargs):
        post = PostModel(**kwargs)
        db.session.add(post)
        db.session.flush()
        return post
    @staticmethod
    def query(page_num, page_size, *args, **kwargs):
        return PostModel.query.paginate(page_num, page_size, error_out=False)