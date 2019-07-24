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
    @staticmethod 
    def queryById(id):
        return PostModel.query.filter_by(id=id).first()
    @staticmethod
    def queryByCategoryId(category_id):
        return PostModel.query.filter_by(category_id=category_id).all()
    @staticmethod
    def deleteById(id):
        PostModel.query.filter_by(id=id).delete()
        db.session.flush()