from datetime import datetime
from . import db
# from sqlalchemy import Integer, String, Text, Column, ForeignKey

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), )
    date = db.Column(db.DateTime, default=datetime.utcnow)
    # category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category')
    tags = db.relationship('Tag')
    content = db.Column(db.Text, default='')

    @staticmethod
    def insert_articles():
        article = {
            'title': 'first',
            'date': datetime.utcnow,
            'content': 'The first content of article.'
        }

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article = db.relationship('Article')

    def __repr__(self):
        return '<Category %r>' % self.category_name


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(30))
    # article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    artilce = db.relationship('Article')

    @staticmethod
    def insert_tags():
        pass

    def __repr__(self):
        return '<Tag %r>' % self.tag_name

# class Article(db.Model):
#     __tablename__ = 'articles'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), )
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#     category = db.Column(db.Integer, db.ForeignKey('categories.id'))
#     content = db.Column(db.Text, default='')
#     tags = db.relationship('Tag', backref='article', lazy='dynamic')

#     def __repr__(self):
#         return '<Article %r>' % self.title


# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String(30))
#     article_id = Column()

#     def __repr__(self):
#         return '<Category %r>' % self.category_name


# class Tag(db.Model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key=True)
#     tag_name = db.Column(db.String(30))
#     article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

#     @staticmethod
#     def insert_tags():
#         pass

#     def __repr__(self):
#         return '<Tag %r>' % self.tag_name
