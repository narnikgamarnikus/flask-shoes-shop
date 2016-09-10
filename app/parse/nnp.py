from bs4 import BeautifulSoup
import urllib.request
import csv
import collections

class Parse():

    def __init__(self, n, k):
        self.link = self.li(n,k)
        self.urllink = self.urllink(self.link)
        self.soup = self.html_soup(self.urllink)
        self.soup_allproducts = self.soup_allproducts(self.soup)
        self.np = self.soup_allproducts(self.soup)
        self.imglist = self.soup_allproducts(self.soup)
        self.linklist = self.soup_allproducts(self.soup)
        self.pg = self.soup_allproducts(self.soup)
        '''
        self.pg = self.soup_allproducts(self.soup)
        self.np = self.soup_allproducts(self.soup)
        self.imglist = self.soup_allproducts(self.soup)
        self.soup_productpage = self.soup_productpage(self.linklist,self.urllink, self.html_soup, n)
        self.gender = self.soup_productpage(self.linklist,self.urllink, self.html_soup, n)
        '''

    def li(self,n, k):
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


    #soup = html_soup(url)
    #print(soup)


    def soup_allproducts(self,soup):
        try:
            pc = soup.find('div', 'row product__container').find_all('a')
            pg = soup.find('h3').span.string[-4:]
            np = soup.find('ul', 'pagination').find_all('li')[-1].string
            pi = soup.find('div', 'row product__container').find_all('img')

            linklist = []
            imglist = []
            for link in pc:
                linklist.append(link.get('href'))
            for img in pi:
                imglist.append(img.get('src'))
        except AttributeError:
            return False
        return self.imglist, self.linklist, self.np, self.pg
    #linklist, pg, np, imglist = soup_allproducts(soup)
    #print (linklist)
    #print(imglist)

    #n = 72
    #url = urllink(link)
    #soup = html_soup(url)

    '''
    def soup_productpage(self, linklist):
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

            return gender, category, brand, model, h1, pricepln, priceusd, priceeur, pricegbp, pricerub, code, fullimglist, smallimglist, hrefimglist, prpchlist, color, colorlink, prpcilist


    gender, category, brand, model, h1, pricepln, priceusd, priceeur, pricegbp, pricerub, code, fullimglist, smallimglist, hrefimglist, prpchlist, color, colorlink, prpcilist = soup_productpage(
        self, linklist)



    print(gender)
    print(category)
    print(brand)
    print(model)
    print(h1)
    print(pricepln)
    print(priceusd)
    print(priceeur)
    print(pricegbp)
    print(pricerub)
    print(code)
    print(color)
    print(colorlink)
    print(fullimglist)
    print(smallimglist)
    print(hrefimglist)
    print(prpchlist)
    print(prpcilist)

    print(prpcilist)
    print(prpchlist)
    print(fullimglist)
    print(smallimglist)
    print(hrefimglist)
    print(gender)
    print(category)
    print(brand)
    print(model)
    print(color)
    print(colorlink)

    #for item in prpcdiv:
        #qwe = prpcdiv.find('a').get('href')
        #asd = prpcdiv.find('img').get('src')
        #prpchlist.append(qwe)
        #prpcilist.append(asd)
#print(prpcilist)
#print(prpchlist)

#print(prpc)
#print(prpcilist)
#print(prpchlist)

#    return h1
#h1 = soup_productpage(linklist,html_soup,urllink)



def soup_content(pc,n):
    try:
        pc, pcount = soup_productpage(soup)
        pcall = pc.find_all('a')
        print(pcall)
        linklist = []
        for link in pcall:
            linklist.append(link.get('href'))
    except AttributeError:
        return False
    return linklist[::2]
linklist = soup_content(pc, n)
'''