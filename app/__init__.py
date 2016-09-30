import os
from flask import (Flask,
    url_for,
    session,
    request,
    abort,
    current_app)
# from flask_login import LoginManager
#from flask_wtf.csrf import CsrfProtect, safe_str_cmp
#from os import path

from .database import db
from werkzeug.contrib.fixers import ProxyFix
import flask_sijax

#import hmac
#from hashlib import sha1

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.wsgi_app = ProxyFix(app.wsgi_app)
    db.init_app(app)
    if app.debug is True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    with app.test_request_context():
        db.create_all()

    from .general import controllers as general
    from .shop import controllers as shop
    from .test import controllers as test
    app.register_blueprint(shop.module)
    app.register_blueprint(general.module)
    app.register_blueprint(test.module)

    flask_sijax.Sijax(app)

    return app
