from flask import (render_template,
                   abort,
                   Blueprint,
                   current_app,
                   g,
                   request,
                   jsonify)

from .models import Products
from datetime import datetime
from time import time,strptime
from random import randint
import flask_sijax



module = Blueprint('shop',
                   __name__)


#@module.context_processor


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/index')
def main():
    np = Products.query.order_by(Products.pub_date.desc()).limit(5).all()
    sp = Products.query.order_by(Products.priceusd.desc()).limit(5).all()
    fp = Products.query.order_by(Products.id).limit(25).all()
    fp = Products.query.order_by(Products.id).limit(25).all()
    lastnote = Products.query.order_by(Products.id.desc()).first()
    print(randint(0,int(lastnote.id)))
    return render_template('shop/index.html',
                           np = np,
                           sp = sp,
                           fp = fp)


@module.route('/<keyword>')
def single_product(keyword):
    sp = Products.query.filter_by(id=keyword).all()
    return render_template('shop/single-product.html',
                           sp=sp)

@module.route('/parse')
def parse():
    from ..parse import parse
    parse = parse.Parse
    k = 1
    while k < 25:
        parse.get_parse(parse,k)
        parse.write_in_base(parse)
        k += 1
