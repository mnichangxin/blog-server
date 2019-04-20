from datetime import datetime
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Integer, String, Text, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Article(Model):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), )
    date = Column(DateTime, default=datetime.utcnow)
    category = relationship('Category')
    tags = relationship('Tag')
    content = Column(Text, default='')

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(30))
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article')

    def __repr__(self):
        return '<Category %r>' % self.category_name


class Tag(Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(30))
    article_id = Column(Integer, ForeignKey('articles.id'))
    artilce = relationship('Article')

    @staticmethod
    def insert_tags():
        pass

    def __repr__(self):
        return '<Tag %r>' % self.tag_name

class User(Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(30))
    intro = Column(Text, default='')

    def __repr__(self):
        return '<User %r>' % self.nickname

