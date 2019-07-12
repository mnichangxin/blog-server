from ..model.common import db
from ..model.tb_category import CategoryModel

class Category:
    @staticmethod
    def insert(**kwargs):
        category = CategoryModel(**kwargs)
        db.session.add(category)
        db.session.flush()
        return category 
    @staticmethod
    def queryById(id):
        return CategoryModel.query.filter_by(id=id).first()
    @staticmethod
    def queryByCategoryName(category_name):
        return CategoryModel.query.filter_by(category_name=category_name).first()
