import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False

    CSRF_ENABLED = True

    SECRET_KEY = 'fjf734md023k474jk92ska'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True