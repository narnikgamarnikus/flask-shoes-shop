from flask import current_app
from app.database import db
from app.shop.models import Products

with app.app_context():
    db.metadata.create_all(db.engine)
    pdf1 = Products(id=1, url='http://worldbox.pl/en/buty-reebok-furylite-slip-on-african-pack-ar1709.html', title='False', brand='False', model='False',article="AR1709", alttitle='BUTY FURYLITE SLIP ON AF BLACK/WHITE/MERLOT/G', pricepln='380', priceusd='100', priceeur='89', pricegbp='76',pricerub='6419', images='[https://m.sportowysklep.pl/2016/reebok/70896/buty-furylite-slip-on-af-blackwhitemerlotg-ar1709-57b6bbf7ac911.jpg]')
    db.session.add(pdf1)
    db.session.commit()