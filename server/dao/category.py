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
    @staticmethod
    def updateByCategoryId(id, **kwargs):
        category = CategoryModel.query.filter_by(id=id).first()
        for k, v in kwargs.items():
            setattr(category, k, v)
        db.session.flush()
        return category
    @staticmethod
    def deleteById(id):
        CategoryModel.query.filter_by(id=id).delete()
        db.session.flush()
