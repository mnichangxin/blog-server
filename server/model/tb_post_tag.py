from sqlalchemy import Integer, Column
from . import db

class PostTagModel(db.Model):
    __tablename__ = 'post_tag'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Post_id %r --- Tag_id %r>' % (self.post_id, self.tag_id)