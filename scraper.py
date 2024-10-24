#!/usr/bin/python
# Scraper.py

from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get('https://www.ebay.com/urw/Available-2010-Titles-Enhanced-Web-Assign-Ser-Calculus-Early-Transcendentals-by-James-Stewart-2007-Hardcover-/product-reviews/53564728?_itm=226310510813')
    soup = BeautifulSoup(response.text, 'html.parser')
    url_list = get_comment_links(soup)
    for url in url_list:
        print(url)

# When given the html document of page 1 of the reviews it extracts the other
# page's urls.
def get_comment_links(soup):
    url_list = []
    for link in soup.find_all('a'):
        if not link.get('href') is None and '&pgn=' in link.get('href'):
            if not link.get('href') in url_list:
                url_list.append(link.get('href'))
    return url_list

if __name__ == '__main__':
    main()
