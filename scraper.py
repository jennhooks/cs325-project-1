#!/usr/bin/python
# Scraper.py

from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get('https://www.ebay.com/urw/Available-2010-Titles-Enhanced-Web-Assign-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2007-Hardcover-/product-reviews/53564728?_itm=226310510813')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    main()
