import datetime
from app.database import db
from datetime import datetime

class Products(db.Model):
    #__tablename__ = 'Products'
    id                      = db.Column(db.Integer, primary_key = True)
    url                     = db.Column(db.String(255), index = True)
    title                   = db.Column(db.String(255), index = True)
    gender                  = db.Column(db.String(64), index = True)
    category                = db.Column(db.String(64), index = True)
    subcategory             = db.Column(db.String(64), index = True)
    model                   = db.Column(db.String(255), index = True)
    pricepln                = db.Column(db.String(64), index=True)
    priceusd                = db.Column(db.String(64), index=True)
    priceeur                = db.Column(db.String(64), index=True)
    pricegbp                = db.Column(db.String(64), index=True)
    pricerub                = db.Column(db.String(64), index=True)
    colorimages             = db.Column(db.String(64), index=True)
    colorlinks              = db.Column(db.String(64), index=True)
    fullimage               = db.Column(db.String(64), index=True)
    smallimage              = db.Column(db.String(64), index=True)
    hrefimage               = db.Column(db.String(64), index=True)
    pub_date                = db.Column(db.DateTime)



    def __init__(self, url, title, gender, category, subcategory, model, pricepln, priceusd, priceeur, pricegbp, pricerub, colorimages, colorlinks, fullimage, smallimage, hrefimage, pub_date=None):
        self.url = url
        self.title = title
        self.gender = gender
        self.category = category
        self.subcategory = subcategory
        self.model = model
        self.pricepln = pricepln
        self.priceusd = priceusd
        self.priceeur = priceeur
        self.pricegbp = pricegbp
        self.pricerub = pricerub
        self.colorimages = colorimages
        self.colorlinks = colorlinks
        self.fullimage = fullimage
        self.smallimage = smallimage
        self.hrefimage = hrefimage
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date




    def __repr__(self):
        return '%r' % self.id + \
               '%r' % self.url + \
               '%r' % self.title + \
               '%r' % self.gender + \
               '%r' % self.category + \
               '%r' % self.subcategory + \
               '%r' % self.model + \
               '%r' % self.pricepln + \
               '%r' % self.priceusd + \
               '%r' % self.priceeur + \
               '%r' % self.pricegbp + \
               '%r' % self.pricerub + \
               '%r' % self.colorimages + \
               '%r' % self.colorlinks + \
               '%r' % self.fullimage + \
               '%r' % self.smallimage + \
               '%r' % self.hrefimage + \
               '%r' % self.pub_date