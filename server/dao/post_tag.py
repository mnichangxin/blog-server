from ..model.common import db
from ..model.tb_post_tag import PostTagModel


class PostTag:
    @staticmethod
    def insert(**kwargs):
        post_tag = PostTagModel(**kwargs)
        db.session.add(post_tag)
        db.session.flush()
        return post_tag
    @staticmethod
    def queryByPostId(post_id):
        return PostTagModel.query.filter_by(post_id=post_id).all()
    @staticmethod
    def queryByPostIdAndTagId(post_id, tag_id):
        return PostTagModel.query.filter_by(post_id=post_id, tag_id=tag_id).first()
    @staticmethod
    def deleteByPostId(post_id):
        PostTag.query.filter_by(post_id=post_id).delete()        
        db.session.flush()