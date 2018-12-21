import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = 'dev'
    DATABASE = os.path.join(basedir, 'instance', 'flaskr.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

config = {
    'default': BaseConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
