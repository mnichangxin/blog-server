from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Integer, String, Text, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

tagging = db.Table('tagging',
                Column('post_id', Integer, ForeignKey('post.id')), 
                Column('tag_id', Integer, ForeignKey('tag.id'))
                )

class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    content = Column(Text, default='')
    date = Column(DateTime, default=datetime.utcnow)
    category = relationship('Category', back_populates='posts')
    tags = relationship('Tag', secondary=tagging, back_populates='posts')
    category_id = Column(Integer, ForeignKey('category.id'))

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(30), unique=True, nullable=False)
    posts = relationship('Post', back_populates='category', cascade='all')

    def __repr__(self):
        return '<Category %r>' % self.category_name

class Tag(db.Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(30), unique=True, nullable=False)
    posts = relationship('Post', secondary=tagging, back_populates='tags', cascade='all')

    def __repr__(self):
        return '<Tag %r>' % self.tag_name


