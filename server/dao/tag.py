from ..model.common import db
from ..model.tb_tag import TagModel

class Tag:
    @staticmethod
    def insert(**kwargs):
        tag = TagModel(**kwargs)
        db.session.add(tag)
