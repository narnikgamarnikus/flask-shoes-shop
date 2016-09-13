from bs4 import BeautifulSoup
import urllib.request
import csv
import collections
import functools
from app.shop.models import Products
from app.database import db


class Parse(object):

    def __init__(self,n,k):

        self.link                   = self.li(n,k)
        self.urllink                = self.urllink(self.link)
        self.soup                   = self.html_soup(self.urllink)
        '''
        self.pg                 = self.count_products(self.html_soup)
        self.pc                 = self.prodoct_link(self.html_soup)
        self.pc_list            = self.prodocts_links_list(self.html_soup)
        self.np                 = self.next_page(self.html_soup)
        self.pi                 = self.product_image(self.html_soup)
        self.pi_list            = self.products_images_list(self.html_soup)

        self.soup_allproducts = self.soup_allproducts(self.soup)
        self.np = self.soup_allproducts(self.soup)
        self.imglist = self.soup_allproducts(self.soup)
        self.linklist = self.soup_allproducts(self.soup)
        self.pg = self.soup_allproducts(self.soup)
        '''

    def li(self,n,k):
        link = 'http://worldbox.pl/en/products/all/item,' + str(n) + '/page,' + str(k)
        return link
    #print (link)

    def urllink(self,link):
        try:
            url = urllib.request.urlopen(link)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return False
            else:
                raise
        return url

    def html_soup(self,url):
        soup = BeautifulSoup(url, 'html.parser')
        return soup

class ParseMainPage(Parse):

    def __init__(self,n,k):
        super().__init__(n,k)
        self.pg                 = self.count_products(self.soup)
        self.pc                 = self.product_link(self.soup)
        self.pc_list            = self.products_links_list(self.soup)
        self.pi                 = self.product_image(self.soup)
        self.pi_list            = self.products_images_list(self.soup)
        self.np                 = self.next_page(self.soup)
    '''
        self.url                    = self.urllink(self.link)
        self.soup                   = self.html_soup(self.url)
        self.pg                     = self.count_products(self.soup)
        self.pc                     = self.product_link(self.soup)
        self.pc_list                = self.products_links_list(self.soup)
        self.pi                     = self.product_image(self.soup)
        self.pi_list                = self.products_images_list(self.soup)
        #self.pclink                = self.product_link_for_parse(self.pc_list, self.x)

        super().__init__(n, k, self.link)
   '''

    def next_page(self,soup):
        try:
            np = soup.find('ul', 'pagination').find_all('li')[-1].string
        except AttributeError:
            return False
        return np

    def count_products(self,soup):
        try:
            pg = soup.find('h3').span.string[-4:]
        except AttributeError:
            return False
        return pg

    def product_link(self,soup):
        try:
            pc = soup.find('div', 'row product__container').find('a').get('href')
        except AttributeError:
            return False
        return pc

    def products_links_list(self,soup):
        try:
            pcl = soup.find('div', 'row product__container').find_all('a')
            pc_list = []
            for link in pcl:
                pc_list.append(link.get('href'))
        except AttributeError:
            return False
        return pc_list[::2]

    def product_image(self,soup):
        try:
            pi = soup.find('div', 'row product__container').find('img').get('src')
        except AttributeError:
            return False
        return pi

    def products_images_list(self,soup):
        try:
            pi_list = []
            pil = soup.find('div', 'row product__container').find_all('img')
            for img in pil:
                pi_list.append(img.get('src'))
        except AttributeError:
            return False
        return pi_list

class ParseProductPage(ParseMainPage, Parse):

    def __init__(self, n, k):
        super().__init__(n, k)
        self.x                  = int(0)
        self.link               = self.product_link_for_parse(self.pc_list, self.x)
        self.urllink            = Parse.urllink(self, self.link)
        self.soup               = self.html_soup(self.urllink)
        self.h1                 = self.h1(self.soup)
        self.code               = self.code(self.soup)
        self.prices             = self.prices(self.soup)
        self.pricepln           = self.pricepln(self.prices)
        self.priceusd           = self.priceusd(self.prices)
        self.priceeur           = self.priceeur(self.prices)
        self.pricegbp           = self.pricegbp(self.prices)
        self.pricerub           = self.pricerub(self.prices)
        self.breadcrumb         = self.breadcrumb(self.soup)
        self.gender             = self.gender(self.breadcrumb)
        self.category           = self.category(self.breadcrumb)
        self.subcategory        = self.subcategory(self.breadcrumb)
        self.model              = self.model(self.breadcrumb)
        self.colorimagelist     = self.colorimages(self.soup)
        self.colorlinklist      = self.colorlinks(self.soup)
        self.fullimagelist      = self.fullimage(self.soup)
        self.smallimagelist     = self.smallimage(self.soup)
        self.hrefimagelist      = self.hrefimage(self.soup)

    def product_link_for_parse(self, pc_list, x):
        self.link = self.pc_list[x]
        return self.link

    def h1(self, soup):
        try:
            h1 = soup.find('h1').span.string
        except AttributeError:
            return False
        return h1

    def code(self,soup):
        try:
            code = soup.find('p', 'product__code').find('span').string
        except AttributeError:
            return False
        return code

    def breadcrumb(self, soup):
        try:
            self.breadcrumb = soup.find('ol', 'breadcrumb').find_all('li')
        except AttributeError:
            return False
        return self.breadcrumb

    def gender(self, breadcrumb):
        try:
            gender = breadcrumb[1].a.string
        except AttributeError:
            return False
        except TypeError:
            return False
        return gender

    def category(self, breadcrumb):
        try:
            category = breadcrumb[2].a.string
        except AttributeError:
            return False
        except TypeError:
            return False
        return category

    def subcategory(self, breadcrumb):
        try:
            subcategory = breadcrumb[3].a.string
        except AttributeError:
            return False
        except TypeError:
            return False
        return subcategory

    def model(self, breadcrumb):
        try:
            model = breadcrumb[4].a.string
        except AttributeError:
            return False
        except TypeError:
            return False
        return model

    def prices(self, soup):
        try:
            prices = soup.find('p', 'product__price').find_all('span')
        except AttributeError:
            return False
        except TypeError:
            return False
        return prices

    def pricepln(self, prices):
        try:
            pricepln = prices[1].string[3:-1]
        except AttributeError:
            return False
        except TypeError:
            return False
        return pricepln

    def priceusd(self, prices):
        try:
            priceusd = prices[2].string[3:-1]
        except AttributeError:
            return False
        except TypeError:
            return False
        return priceusd

    def priceeur(self, prices):
        try:
            priceeur = prices[3].string[3:-1]
        except AttributeError:
            return False
        except TypeError:
            return False
        return priceeur

    def pricegbp(self, prices):
        try:
            pricegbp = prices[4].string[3:-1]
        except AttributeError:
            return False
        except TypeError:
            return False
        return pricegbp

    def pricerub(self, prices):
        try:
            pricerub = prices[5].string[3:-1]
        except AttributeError:
            return False
        except IndexError:
            return False
        return pricerub

    def colorimages(self, soup):
        try:
            z = 0
            colorimagelist = []
            colors = soup.find('div', 'product__color').find_all('div', 'col-sm-2 col-xs-4 col-md-3')
            for item in colors:
                colorimage = colors[z].find_all('img')[0].get('src')
                colorimagelist.append(colorimage)
                z += 1
        except AttributeError:
            return False
        except IndexError:
            return False
        return colorimagelist

    def colorlinks(self, soup):
        try:
            z = 0
            colorlinklist = []
            colors = soup.find('div', 'product__color').find_all('div', 'col-sm-2 col-xs-4 col-md-3')
            for item in colors:
                colorlink = colors[z].find_all('a')[0].get('href')
                colorlinklist.append(colorlink)
                z += 1
        except AttributeError:
            return False
        except IndexError:
            return False
        return colorlinklist

    def fullimage(self, soup):
        try:
            z = 0
            fullimagelist = []
            fullimages = soup.find('div', 'col-md-8 col-sm-12').find_all('a')
            for item in fullimages:
                fullimagelist.append(fullimages[z].get('data-full'))
                z += 1
        except IndexError:
            return False
        except AttributeError:
            return False
        return fullimagelist

    def smallimage(self, soup):
        try:
            z = 0
            smallimagelist = []
            smallimages = soup.find('div', 'col-md-8 col-sm-12').find_all('a')
            for item in smallimages:
                smallimagelist.append(smallimages[z].get('data-thumb'))
                z += 1
        except AttributeError:
            return False
        except IndexError:
            return False
        return smallimagelist

    def hrefimage(self, soup):
        try:
            z = 0
            hrefimagelist = []
            hrefimages = soup.find('div', 'col-md-8 col-sm-12').find_all('a')
            for item in hrefimages:
                hrefimagelist.append(hrefimages[z].get('href'))
                z += 1
        except AttributeError:
            return False
        except IndexError:
            return False
        return hrefimagelist

class Parsing(ParseProductPage,ParseMainPage,Parse):

    def parsing(self,n,k):
        while self.np is int:
            asd = self.product_link_for_parse(self.pc_list, self.x)
            print(asd)
        k += 1
        return k
        #p = Parse(n,k)
        #pmp = ParseMainPage(n,k)
'''
            p = -1
            while p < n+1:
                ppp = ParseProductPage(n,k)
                ppp.product_link_for_parse(ppp.pc_list, ppp.x)
                product = Products(url              =ppp.link,
                                    title           =ppp.h1,
                                    gender          =ppp.gender,
                                    category        =ppp.category,
                                    subcategory     =ppp.subcategory,
                                    model           =ppp.model,
                                    pricepln        =ppp.pricepln,
                                    priceusd        =ppp.priceusd,
                                    priceeur        =ppp.priceeur,
                                    pricegbp        =ppp.pricegbp,
                                    pricerub        =ppp.pricerub,
                                    colorimages     =ppp.colorimages,
                                    colorlinks      =ppp.colorlinks,
                                    fullimage       =ppp.fullimage,
                                    smallimage      =ppp.smallimage,
                                    hrefimage       =ppp.hrefimage)
                db.create_all()
                db.session.add(product)
                db.session.commit()
                p += 1
            k += 1

    def soup_productpage(self, linklist, pc_list):
        z = 0
        while z < int(n) + 1:
            link = linklist[z]
            print('Parsed link: ' + str(link))
            url = self.urllink(link)
            soup = self.html_soup(url)
            if soup.find('ol', 'breadcrumb') is str:
                breadcrumb = soup.find('ol', 'breadcrumb')
                gender = breadcrumb[1].a.string
                category = breadcrumb[2].a.string
                brand = breadcrumb[3].a.string
                model = breadcrumb[4].a.string
            else:
                gender = 'Gender is not found'
                category = 'Category is not found'
                brand = 'Brand is ot found'
                model = 'Model is not found'
                print('hello')
            h1 = soup.find('h1').span.string
            prices = soup.find('p', 'product__price').find_all('span')
            pricepln = prices[0].string[3:6]
            priceusd = prices[1].string[3:6]
            priceeur = prices[2].string[3:6]
            pricegbp = prices[3].string[3:6]
            pricerub = prices[4].string[3:7]
            code = soup.find('p', 'product__code').find('span').string
            fullimglist = []
            smallimglist = []
            hrefimglist = []
            prpcilist = []
            prpchlist = []
            prpcimages = soup.find('div', 'col-md-8 col-sm-12').find_all('a')
            x = - 1
            for item in prpcimages:
                x += 1
                fullimglist.append(prpcimages[x].get('data-full'))
                smallimglist.append(prpcimages[x].get('data-thumb'))
                hrefimglist.append(prpcimages[x].get('href'))
            colors = soup.find('div', 'product__color').find_all('div', 'col-sm-2 col-xs-4 col-md-3')
            x = - 1
            for item in colors:
                x += 1
                colorlink = colors[x].find_all('a')[0].get('href')
                prpcilist.append(colorlink)
                color = colors[x].find_all('img')[0].get('src')
                prpchlist.append(color)

        super().__init__(n, k)
    '''