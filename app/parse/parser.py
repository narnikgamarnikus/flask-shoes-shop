from bs4 import BeautifulSoup
import urllib.request
import csv

k = 1

def read_csv(k):
    with open('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/products_links2.csv') as f:
        r = csv.reader(f)
        cont = [row for row in r]
        d = (cont[k])[0]
    return d
d = read_csv(k)
print (d)


def get_url(d):
    try:
        url = urllib.request.urlopen(d)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return False
        else:
            raise
    return url
url = get_url(d)


def get_title(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        h1 = soup.find('h1')
        title = h1.find_all('span')[-1].string
    except AttributeError:
        return False
    return title
title = get_title(url)
print(title)
'''
def get_description(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        description = soup.find_all('div', 'panel-collapse collapse in')
        print(description)
        cont = [row for row in description]
    except AttributeError:
            return False
    return cont
cont = get_description(url)
print (cont)

def get_gender(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        ol = soup.find('ol', 'breadcrumb')
        brand = ol.find_all('a')[0].string
    return brand
'''