from bs4 import BeautifulSoup
import urllib.request
import csv
import collections

n = 72
k = 1

def li(k):
    link = 'http://worldbox.pl/en/products/all/item,' + str(n) + '/page,' + str(k)
    return link
link = li(k)
#print (link)

def urllink(link):
    try:
        url = urllib.request.urlopen(link)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return False
        else:
            raise
    return url, urllink
url, urllink = urllink(link)


def html_soup(url):
    soup = BeautifulSoup(url, 'html.parser')
    return soup, html_soup
soup, html_soup = html_soup(url)


#soup = html_soup(url)
#print(soup)


def soup_allproducts(soup):
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
    return linklist[::2],pg,np,imglist
linklist, pg, np, imglist = soup_allproducts(soup)
#print (linklist)
#print(imglist)

#def soup_productpage(linklist,html_soup,urllink):
link = linklist[0]
print (link)
url, urllink = urllink(link)
soup, html_soup = html_soup(url)
h1 = soup.find('h1').span.string
pr = soup.find('p', 'product__price').find_all('span')[0].string


print(pr)
#    return h1
#h1 = soup_productpage(linklist,html_soup,urllink)


'''
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