from bs4 import BeautifulSoup
import urllib.request
import re


def parse_price(sku=None):
    url = f"https://www.cdiscount.com/f-0-{sku}.html"
    with urllib.request.urlopen(url) as resp:

        lien = r'<link rel="canonical" href="https://www.cdiscount.com/" />'
        data = resp.read()

        if re.findall(lien, str(data)):
            return False

        elif sku is None:
            return False

        else:
            soup = BeautifulSoup(data, 'html.parser')
            classe = 'fpPrice price jsMainPrice jsProductPrice hideFromPro'
            element = str(soup.find_all('span', {'class': classe}))
            prix = float(re.findall(r'content="(.*?)"', element)[0])
            return prix
