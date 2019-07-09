from ..model.common import db
from ..model.category import CategoryModel

class Category:
    @staticmethod
    def insert(**kwargs):
        db.session.add(CategoryModel(**kwargs))
    @staticmethod
    def queryById(id):
        return CategoryModel.query.filter_by(id=id).first()
    @staticmethod
    def queryByCategoryName(category_name):
        return CategoryModel.query.filter_by(category_name=category_name).first()