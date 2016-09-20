import os
from flask import (Flask,
                   redirect,
                   url_for,
                   session,
                   request,
                   abort,
                   current_app)
# from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect, safe_str_cmp
from os import path

from .database import db
from werkzeug.contrib.fixers import ProxyFix
import flask_sijax

import hmac
from hashlib import sha1

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

    @app.before_request
    def check_csrf_token():
        """Checks that token is correct, aborting if not"""
        if request.method in ("GET",):  # not exhaustive list
            return
        token = request.form.get("csrf_token")
        if token is None:
            app.logger.warning("Expected CSRF Token: not present")
            abort(400)
        if not safe_str_cmp(token, csrf_token()):
            app.logger.warning("CSRF Token incorrect")
            abort(400)

    @app.template_global('csrf_token')
    def csrf_token():
        """
        Generate a token string from bytes arrays. The token in the session is user
        specific.
        """
        if "_csrf_token" not in session:
            session["_csrf_token"] = os.urandom(128)
        return hmac.new(app.secret_key, session["_csrf_token"],
                        digestmod=sha1).hexdigest()

    def log_error(*args, **kwargs):
        current_app.logger.error(*args, **kwargs)

    CsrfProtect(app)

    return app
