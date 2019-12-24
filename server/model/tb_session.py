from sqlalchemy import String, Integer, Column
from . import db

class SessionModel(db.Model):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    session_id = Column(String(32), unique=True, nullable=True)

    def __repr__(self):
        return '<Session %r>' % self.session_id