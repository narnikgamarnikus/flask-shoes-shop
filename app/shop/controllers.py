from flask import (render_template,
                   abort,
                   Blueprint,
                   current_app)

module = Blueprint('shop',
                   __name__)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/')
def single_product():
    return render_template('shop/single-product.html')

