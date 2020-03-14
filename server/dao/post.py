from server.model import db
from server.model.tb_post import PostModel

class Post:
    @staticmethod
    def insert(**kwargs):
        post = PostModel(**kwargs)
        db.session.add(post)
        db.session.flush()
        return post
    @staticmethod
    def query(page_num, page_size, *args, **kwargs):
        return PostModel.query.filter_by(**kwargs).paginate(page_num, page_size, error_out=False)
    @staticmethod 
    def queryById(id):
        return PostModel.query.filter_by(id=id).first()
    @staticmethod
    def queryByCategoryId(category_id):
        return PostModel.query.filter_by(category_id=category_id).all()
    @staticmethod
    def queryByPostIds(page_num, page_size, post_ids):
        return PostModel.query.filter(PostModel.id.in_(post_ids)).paginate(page_num, page_size, error_out=False)
    @staticmethod
    def updateById(id, **kwargs):
        post = PostModel.query.filter_by(id=id).first()
        for k, v in kwargs.items():
            setattr(post, k, v)
        db.session.flush()
        return post
    @staticmethod
    def deleteById(id):
        PostModel.query.filter_by(id=id).delete()
        db.session.flush()