import datetime
from app.database import db
from datetime import datetime

class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(255), index = True)
    title = db.Column(db.String(255), index = True)
    brand = db.Column(db.String(64), index = True)
    model = db.Column(db.String(64), index = True)
    article = db.Column(db.String(64), index = True)
    alttitle = db.Column(db.String(255), index = True)
    pricepln = db.Column(db.String(64), index=True)
    priceusd = db.Column(db.String(64), index=True)
    priceeur = db.Column(db.String(64), index=True)
    pricegbp = db.Column(db.String(64), index=True)
    pricerub = db.Column(db.String(64), index=True)
    images = db.Column(db.String(64), index=True)
    pub_date = db.Column(db.DateTime)

    def __init__(self, url, title, brand, model, article, alttitle, pricepln, priceusd, priceeur, pricegbp, pricerub, images, pub_date=None):
        self.url = url
        self.title = title
        self.brand = brand
        self.model = model
        self.article = article
        self.alttitle = alttitle
        self.pricepln = pricepln
        self.priceusd = priceusd
        self.priceeur = priceeur
        self.pricegbp = pricegbp
        self.pricerub = pricerub
        self.images = images
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '%r' % self.id + \
               '%r' % self.url + \
               '%r' % self.title + \
               '%r' % self.brand + \
               '%r' % self.model + \
               '%r' % self.article + \
               '%r' % self.alttitle + \
               '%r' % self.pricepln + \
               '%r' % self.priceusd + \
               '%r' % self.priceeur + \
               '%r' % self.pricegbp + \
               '%r' % self.pricerub + \
               '%r' % self.images + \
               '%r' % self.pub_date