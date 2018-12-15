import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = 'dev'
    DATABASE = os.path.join(basedir, 'instance', 'flaskr.sqlite')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
class TestingConfig(BaseConfig):
    TESTING = True

config = {
    'default': BaseConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}