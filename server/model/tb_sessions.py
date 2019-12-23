from sqlalchemy import String, Column
from . import db

class SessionsModel(db.Model):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    session_id = Column(String(30), unique=True, nullable=True)

    def __repr__(self):
        return '<Sessions %r>' % self.session_id