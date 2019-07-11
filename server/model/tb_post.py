from sqlalchemy import Integer, String, Text, DateTime, Column
from .common import db

class PostModel(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    content = Column(Text)
    category_id = Column(Integer)
    created_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime)

    def __repr__(self):
        return '<Post %r>' % self.title