from flask import (render_template,
                   Blueprint,
                   current_app,
                   g,
                   request)

from .models import Products
import flask_sijax
from sijax.plugin.comet import register_comet_object



module = Blueprint('shop',
                   __name__)



class SijaxHandler(object):

    @staticmethod
    def create_card(obj_response):
        count = 1
        case = """
        <a class="shop-link" href="cart.html" title="View my shopping cart">
        <i class="fa fa-shopping-cart cart-icon"></i>
        <b>Корзина</b>
        <span class="ajax-cart-quantity" id="count">%s</span>
        </a>
                """ % count
        total = """
        <div id="shopcard">
        </div>
        <div class="shipping-total-bill">
        <div class="cart-prices">
        <span class="shipping-cost">$</span>
        <span>Shipping</span>
        </div>
        <div class="total-shipping-prices">
        <span class="shipping-total">$</span>
        <span>Total</span>
        </div>
        </div>
                """
        obj_response.html_append('#shoppingcart', case)
        obj_response.html_append('#cardlist', total)




    @staticmethod
    def add_to_card(obj_response, id):
        i=0
        product = Products.query.filter(Products.id == id).one()
        obj_response.script("$('#count').text('%s')"%i)
        i=+1
        item = """
                <div class="shipping-item" id="%s">
                <span class="cross-icon"><i class="fa fa-times-circle" onclick="sjxComet.request('delete', ['{{product.id}}']);"></i></span>
                <div class="shipping-item-image">
                <a href="%s">
                <img src="{{ url_for('images.fit',
                filename=%s,
                transform=transform,
                enlarge=enlarge,
                width=50,
                height=50,
                quality=90,
            ) }}" />"</a>
                </div>
                <div class="shipping-item-text">
                <span>1 <span class="pro-quan-x">x</span> <a href="%s" class="pro-cat">%s</a></span>
                <span class="pro-quality"><a href="%s">%s</a></span>
                <p>$%s</p>
                </div>
                </div>
                """ % (i, product.url.split('/')[4], product.smallimage[2:-2].split("', '")[0], product.url.split('/')[4], product.title, product.url.split('/')[4], product.title, str(product.priceusd[:-3]))


        #obj_response.script("$('#count').text('%s');" % i)
        #obj_response.html_append('#shoppingcart', case)
        obj_response.html_append('#shopcard', item)


    def delete(obj_response):
        obj_response.html('#%s', '' %i)



        #obj_response.script("$('#count').text('%s');" % i)




@flask_sijax.route(module, '/index')
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
    return dict(Products=Products)

