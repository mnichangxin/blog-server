from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

Base = declarative_base()

class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    post = relationship('Post', back_populates='tag')
    tag = relationship('Tag', back_populates='post')

class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    content = Column(Text, default='')
    date = Column(DateTime, default=datetime.utcnow)
    category = relationship('Category', back_populates='post')
    tag = relationship('Association', back_populates='post')
    category_id = Column(Integer, ForeignKey('category.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(30))
    posts = relationship('Post', cascade='all', back_populates='category')

    def __repr__(self):
        return '<Category %r>' % self.category_name

class Tag(db.Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(30))
    posts = relationship('Association', cascade='all', back_populates='tag')

    def __repr__(self):
        return '<Tag %r>' % self.tag_name


