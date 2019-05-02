from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# tagging = db.Table('tagging',
#                 Column('post_id', Integer, ForeignKey('post.id')), 
#                 Column('tag_id', Integer, ForeignKey('tag.id'))
#                 )



