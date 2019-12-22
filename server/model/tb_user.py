from sqlalchemy import Integer, String, Column
from . import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(100), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username