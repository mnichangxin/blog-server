from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .post import PostModel
from .category import CategoryModel
from .tag import TagModel