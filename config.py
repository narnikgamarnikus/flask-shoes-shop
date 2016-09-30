import os, sys
BASEDIR = os.path.abspath(os.path.dirname(__file__))

path = os.path.join('.', os.path.dirname(__file__), '../')
sys.path.append(path)

class Config(object):
    DEBUG = False

    CSRF_ENABLED = True

    SECRET_KEY = 'iddqd3133122'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SIJAX_JSON_URI = '/static/js/sijax/json2.js'
    SIJAX_STATIC_PATH = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = False
