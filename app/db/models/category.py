from sqlalchemy import Integer, String, Column
from . import db

class CategoryModel(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.category_name