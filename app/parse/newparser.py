from bs4 import BeautifulSoup
import urllib.request
import csv
import collections

from app.shop.models import Products
from app.database import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from flask import abort

class Parse:

    Category = collections.namedtuple("Category", "pos element1 element2 method")

    def __init__(self, k):
        self.data = {'title': Category(-1, 'ol', 'li', 'breadcrumb'),
                    'gender': Category(0, 'ol', 'a', 'breadcrumb'),
                    'category': Category(1, 'ol', 'a', 'breadcrumb'),
                    'model': Category(2, 'ol', 'a', 'breadcrumb'),
                    'article': Category(0, 'p', 'span', 'product_code'),
                    'article2': Category(0, 'h1', 'span', '')}
    k = 1



    def csv(k):
        with open('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/products_links2.csv') as f:
            r = csv.reader(f)
            cont = [row for row in r]
            link = (cont[k])[0]
            return link

    link = csv(k)

    def url(link):
        try:
            url = urllib.request.urlopen(link)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return False
            else:
                raise
        return url
    url = url(link)

    def page(url):
        try:
            page = BeautifulSoup(url, 'html.parser')
        except AttributeError:
            return False
        return page
    page = page(url)
    print(page)


'''
    def get_title(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            h1 = soup.find('h1')
            title = h1.find_all('span')[-1].string
        except AttributeError:
            return False
        return title

    def get_gender(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            ol = soup.find('ol', 'breadcrumb')
            gender = ol.find_all('a')[0].string
        except AttributeError:
            return False
        return gender

    def get_category(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            ol = soup.find('ol', 'breadcrumb')
            brand = ol.find_all('a').get_text[1].string
        except AttributeError:
            return False
        return brand


    def get_model(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            ol = soup.find('ol', 'breadcrumb')
            model = ol.find_all('a')[2].string
        except AttributeError:
            return False
        return model


    def get_article(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            product_code = soup.find('p', 'product__code')
            article = product_code.find_all('span')[0].string
        except AttributeError:
            return False
        return article


    def get_article_2(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            geth1 = soup.find('h1')
            article_2 = geth1.find_all('span')[0].string
        except AttributeError:
            return False
        return article_2


    def get_prices(url):
        try:
            soup = BeautifulSoup(url, 'html.parser')
            product_price = soup.find_all('span', 'select_currency currency hide')
        except AttributeError:
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


    def get_parse(self,k):
        self.d = self.read_csv(k)
        self.url = self.get_url(self.d)
        self.title = self.get_title(self.url)
        self.url = self.get_url(self.d)
        self.gender = self.get_gender(self.url)
        self.url = self.get_url(self.d)
        self.category = self.get_category(self.url)
        self.url = self.get_url(self.d)
        self.model = self.get_model(self.url)
        self.url = self.get_url(self.d)
        self.article = self.get_article(self.url)
        self.url = self.get_url(self.d)
        self.article_2 = self.get_article_2(self.url)
        self.url = self.get_url(self.d)
        self.prices = self.get_prices(self.url)
        self.price_pln = self.prices[0].string[3:6]
        self.price_usd = self.prices[1].string[3:6]
        self.price_eur = self.prices[2].string[3:6]
        self.price_gbp = self.prices[3].string[3:6]
        self.price_rub = self.prices[4].string[3:7]
        self.url = self.get_url(self.d)
        self.images = self.get_img(self.url)[0]
        return self.d, \
               self.title, \
               self.gender, \
               self.category, \
               self.model, \
               self.article, \
               self.article_2, \
               self.images, \
               self.price_pln, \
               self.price_usd, \
               self.price_eur, \
               self.price_gbp, \
               self.price_rub, \
               self.images

    def write_in_base(self):
        self.product = Products(id          = 3,
                                url         = self.d,
                                title       = self.title,
                                brand       = self.gender,
                                model       = self.model,
                                article     = self.article,
                                alttitle    = self.article_2,
                                pricepln    = self.price_pln,
                                priceusd    = self.price_usd,
                                priceeur    = self.price_eur,
                                pricegbp    = self.price_gbp,
                                pricerub    = self.price_rub,
                                images      = self.images )
        db.create_all()
        db.session.add(self.product)
        db.session.commit()
        return self.product
'''