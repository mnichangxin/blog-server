from datetime import datetime
from . import db


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=30))
    date = db.Column(db.Datetime, default=datetime.utcnow)
    category = db.Column()

    def __repr__(self):
        return '<Article %r>' % self.title


class category(db.Model):
    __tablename__ = 'categories'
    article_id = db.Column(db.Integer)
    category_name = db.Column(db.String(length=30))

    def __repr__():
        return '<Category %r>' % self.category_name
