from sqlalchemy import Integer, String, Column
from .. import db

class TagModel(db.Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tag_name