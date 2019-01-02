from datetime import datetime
from . import db


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    date = db.Column(db.Datetime, default=datetime.utcnow)
    category = db.Column(db.String(30), db.Foreignkey('categories.id'))
    content = db.Column(db.Text, default='')
    tags = db.relationship('Tag', backref='article', lazy='dynamic')

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer)
    category_name = db.Column(db.String(30))

    def __repr__(self):
        return '<Category %r>' % self.category_name


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer)
    tag_name = db.Column(db.String(30))
    article_id = db.Column(db.Integer, db.Foreignkey('articles.id'))

    def __repr__(self):
        return '<Tag %r>' % self.tag_name
