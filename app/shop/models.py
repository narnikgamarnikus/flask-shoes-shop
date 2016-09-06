from app.database import db

class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True, unique = True)
    url = db.Column(db.String(255), index = True,)
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

    def __init__(self,id, url, title, brand, model, article, alttitle, pricepln, priceusd, priceeur, pricegbp, pricerub, images):
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

    def __repr__(self):
        return 'Alternative Title: %r ' % (self.alttitle)
