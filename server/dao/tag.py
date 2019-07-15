from ..model.common import db
from ..model.tb_tag import TagModel

class Tag:
    @staticmethod
    def insert(**kwargs):
        tag = TagModel(**kwargs)
        db.session.add(tag)
        db.session.flush()
        return tag
    @staticmethod
    def queryByTagId(tag_id):
        return TagModel.query.filter_by(tag_id=tag_id).first()
    @staticmethod
    def queryByTagName(tag_name):
        return TagModel.query.filter_by(tag_name=tag_name).first()

