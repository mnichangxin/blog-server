from datetime import datetime
from sqlalchemy import Integer, String, Text, DateTime, Column
from . import db

class PostModel(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    content = Column(Text, default='')
    first_date = Column(DateTime, nullable=False)
    last_date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title