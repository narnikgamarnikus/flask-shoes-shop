from bs4 import BeautifulSoup
import urllib.request
import csv
#from app.shop.models import Products
#from app.database import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from flask import abort


k = 1


def read_csv(k):
    with open('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/products_links2.csv') as f:
        r = csv.reader(f)
        cont = [row for row in r]
        d = (cont[k])[0]
        return d


def get_url(d):
    try:
        url = urllib.request.urlopen(d)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return False
        else:
            raise
    return url


def get_title(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        ol = soup.find('ol', 'breadcrumb')
        title = ol.find_all('li')[-1].string
    except AttributeError:
        return False
    return title


def get_brand(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        ol = soup.find('ol', 'breadcrumb')
        brand = ol.find_all('a')[2].string
    except AttributeError:
        return False
    except IndexError:
        return False
    return brand


def get_model(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        ol = soup.find('ol', 'breadcrumb')
        model = ol.find_all('a')[3].string
    except AttributeError:
        return False
    except IndexError:
        return False
    return model


def get_article(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        product_code = soup.find('p', 'product__code')
        article = product_code.find_all('span')[0].string
    except AttributeError:
        return False
    except IndexError:
        return False
    return article


def get_article_2(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        geth1 = soup.find('h1')
        article_2 = geth1.find_all('span')[0].string
    except AttributeError:
        return False
    except IndexError:
        return False
    return article_2


def get_prices(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        product_price = soup.find_all('span', 'select_currency currency hide')
    except AttributeError:
        return False
    except IndexError:
        return False
    return product_price


def get_img(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        div = soup.find_all('div', 'fotorama fotorama-primary')
        for a in div:
            b = a.find_all('a')
            images = []
            for c in b:
                d = c['data-full']
                images.append(d)
    except AttributeError:
        return False
    return images

while k < 2714:
	print('Получили k равный ' + str(k))
	d = read_csv(k)
	print('Посетили страницу ' + str(d))
	url = get_url(d)
	title = get_title(url)
	print('Спарсили титул ' + str(title))
	url = get_url(d)
	brand = get_brand(url)
	print('Спарсили бренд ' + str(brand))
	url = get_url(d)
	model = get_model(url)
	print('Спарсили модель ' + str(model))
	url = get_url(d)
	article = get_article(url)
	print('Спарсили артикул ' + str(article))
	url = get_url(d)
	article_2 = get_article_2(url)
	print('Спарсили альтернативный титул ' + str(article_2))
	url = get_url(d)
	product_price = get_prices(url)
	print('Спарсили цену ' + str((product_price[0].string)[3:6]) + ' PLN')
	url = get_url(d)
	product_price = get_prices(url)
	print('Спарсили цену ' + str((product_price[1].string)[3:6]) + ' USD')
	url = get_url(d)
	product_price = get_prices(url)
	print('Спарсили цену ' + str((product_price[2].string)[3:6]) + ' EUR')
	url = get_url(d)
	product_price = get_prices(url)
	print('Спарсили цену ' + str((product_price[3].string)[3:6]) + ' GBP')
	url = get_url(d)
	product_price = get_prices(url)
	print('Спарсили цену ' + str((product_price[4].string)[3:7]) + ' RUB')
	url = get_url(d)
	images = get_img(url)
	print('Спарсили картинку ' + str(images))
    try:
	    product = Products(id = k,
		    			   url = d,
		    			   title = title,
		    			   brand = brand,
		    			   model = model,
		    			   article = article,
		    			   alttitle = article_2,
		    			   pricepln = (product_price[0].string)[3:6],
		    			   priceusd = (product_price[1].string)[3:6],
		    			   priceeur = (product_price[2].string)[3:6],
		    			   pricegbp = (product_price[3].string)[3:6],
		    			   pricerub = (product_price[4].string)[3:7],
		    			   images = images)
	    print('product' + str(k) + 'готов к записи в базу данных')
	    db.session.add(product)
	    db.session.commit()
        print('product' + str(k) + 'записан а базу данных')
        k + 1
    except SQLAlchemyError as e:
        log_error('There was error while querying database', exc_info=e)
        db.session.rollback()
        flash('Uncaught exception while querying database', 'danger')
        abort(500)


