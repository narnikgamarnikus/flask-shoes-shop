from flask import (render_template,
                   Blueprint,
                   current_app,
                   g,
                   request)

from .models import Products
#import flask_sijax
#from sijax.plugin.comet import register_comet_object
from jinja2schema import infer, to_json_schema
import json
from collections import defaultdict

module = Blueprint('shop',
                   __name__)


@module.route('/index')
def index():
    #fp = query.order_by(Products.id).limit(25).all()
    #wc = Products.query.group_by(Products.category).all()
    query = Products.query
    np = query.order_by(Products.pub_date.desc()).limit(5).all()
    sp = query.order_by(Products.priceusd.desc()).limit(5).all()
    fp = query.order_by(Products.id).limit(25).all()
    if g.sijax.is_sijax_request:
        g.sijax.register_comet_object(SijaxHandler)
        return g.sijax.process_request()

    return render_template('shop/index.html',
        fp=fp,
        np=np,
        sp=sp)

'''
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
'''

@module.route('/shop-grid')
def shop_grid():
    return render_template('shop/shop-gird.html')


@module.route('/<keyword>')
def single_product(keyword):
    query = Products.query
    sp = query.filter(Products.url.endswith(keyword))
    return render_template('shop/single-product.html', sp=sp)


@module.route('/parse')
def parse():
    from ..parse import parsing
    return render_template('parse/parse.html')


@module.context_processor
def menu():
    q = Products.query
    genders = q.filter(Products.gender !=0).group_by(Products.gender)
    categories = q.filter(Products.category != 0, Products.category != 'Clothing').group_by(Products.category).all()
    gen = {
        gender.gender: {
            category.category: {
                subcategory.subcategory for subcategory in q.filter(Products.gender == gender.gender, Products.category == category.category, Products.subcategory != 0).group_by(Products.subcategory)
            } for category in categories
        } for gender in genders
    }
    
    gen = json.dumps(gen, default=lambda obj: list(obj) if isinstance(obj, set) else "raise TypeError")
    gen = json.loads(gen)

    return dict(gen=gen)

