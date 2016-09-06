import os
from flask import Flask
# from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from .database import db
from werkzeug.contrib.fixers import ProxyFix


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.wsgi_app = ProxyFix(app.wsgi_app)
    db.init_app(app)
    '''
    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass
    '''
    with app.test_request_context():
        db.create_all()

    from .general import controllers as general
    from .shop import controllers as shop
    app.register_blueprint(shop.module)
    app.register_blueprint(general.module)

    CsrfProtect(app)

    return app
