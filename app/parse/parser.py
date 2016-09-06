from bs4 import BeautifulSoup
import urllib.request
import csv

k = 1

def read_csv(k):
    with open('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/products_links2.csv') as f:
        r = csv.reader(f)
        print(r)
        cont = [row for row in r]
        print(cont)
        d = (cont[k])[0]
        return d
d = read_csv(k)
print(d)

'''
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

def get_gender(url):
    try:
        soup = BeautifulSoup(url, 'html.parser')
        ol = soup.find('ol', 'breadcrumb')
        brand = ol.find_all('a')[0].string
    return brand
'''