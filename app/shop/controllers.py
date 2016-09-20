from flask import (render_template,
                   Blueprint,
                   current_app,
                   g,
                   request)

from .models import Products
import flask_sijax




module = Blueprint('shop',
                   __name__)


@flask_sijax.route(module, '/')
def main():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    return render_template('shop/base.html',
        v='BYN')


@module.route('/index')
def index():
    query = Products.query
    np = query.order_by(Products.pub_date.desc()).limit(5).all()
    sp = query.order_by(Products.priceusd.desc()).limit(5).all()
    fp = query.order_by(Products.id).limit(25).all()
    #fp = query.order_by(Products.id).limit(25).all()
    #wc = Products.query.group_by(Products.category).all()

    return render_template('shop/index.html',
                           np=np,
                           sp=sp,
                           fp=fp)


@module.route('/shop-grid')
def shop_grid():
    return render_template('shop/shop-gird.html')


@module.route('/<keyword>')
def single_product(keyword):
    query = Products.query
    sp = query.filter(Products.url.endswith(keyword))
    return render_template('shop/single-product.html',
                           sp=sp)


@module.route('/parse')
def parse():
    from ..parse import parsing
    return render_template('parse/parse.html')


@module.context_processor
def menu():
    return dict(Products=Products)


def price():
    return dict(price=price)

