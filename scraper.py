#!/usr/bin/python
# Scraper.py

from bs4 import BeautifulSoup
import requests

def main():
    product_url_list = get_product_links()
    # Product 1
    response = requests.get(product_url_list[0])
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = get_reviews(soup)
    for review in reviews:
        print(review)

# Returns a list of strings where each entry in the list is one review from the page.
def get_reviews(soup):
    review_list = []
    for content in soup.find_all('p', itemprop="reviewBody"):
        review_list.append(content.text)
    return review_list

# Returns the list of product urls in the input file.
def get_product_links():
    url_list = []
    input_filename = 'input.txt'
    with open(input_filename, 'r') as file:
        for line in file:
            url_list.append(line.rstrip())
    return url_list

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
