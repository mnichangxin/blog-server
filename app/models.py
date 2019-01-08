from datetime import datetime
from . import db


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), )
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    content = db.Column(db.Text, default='')
    tags = db.relationship('Tag', backref='article', lazy='dynamic')

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30))

    def __repr__(self):
        return '<Category %r>' % self.category_name


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(30))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    # @staticmethod
    # def insert_tags():
    def __repr__(self):
        return '<Tag %r>' % self.tag_name
