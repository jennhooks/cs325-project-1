#!/usr/bin/python
# Scraper.py

from bs4 import BeautifulSoup
import requests

def main():
    # Get urls from input file.
    product_url_list = get_product_links()
    # Define names for the output files.
    product_versions = ['5th edition', '6th edition', '7th edition', '8th edition']
    # Associate the urls with the output file names.
    product_dict = {}
    for i in range(0, len(product_url_list)):
        product_dict[product_url_list[i]] = product_versions[i]

    for product in product_dict:
        all_reviews = get_all_reviews(product)
        save_reviews(all_reviews, product_dict[product])

# Saves the list of review strings to a file named 'PREFIX_reviews.txt'
def save_reviews(reviews, file_prefix):
    output_filename = file_prefix + ' reviews'
    with open(output_filename, 'w') as file:
        for review in reviews:
            file.write(review)
            file.write('\n')

# Returns a list containing all reviews for a product.
def get_all_reviews(url):
    review_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = get_review_links(soup)
    # If the product only has one page of reviews this list will be empty
    # because products with only one page of reviews don't have anything
    # to extract urls from.
    if not urls:
        urls = [url]
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        review_list.extend(get_reviews(soup))
    return review_list

# Returns a list of strings where each entry in the list is one review from the page.
def get_reviews(soup):
    review_list = []
    for content in soup.find_all('p', itemprop="reviewBody"):
        review_list.append(content.text.replace('Read full review...', ''))
    return review_list

# When given the html document of page 1 of the reviews it extracts the other
# page's urls.
def get_review_links(soup):
    url_list = []
    for link in soup.find_all('a'):
        if not link.get('href') is None and '&pgn=' in link.get('href'):
            if not link.get('href') in url_list:
                url_list.append(link.get('href'))
    return url_list

# Returns the list of product urls in the input file.
def get_product_links():
    url_list = []
    input_filename = 'input.txt'
    with open(input_filename, 'r') as file:
        for line in file:
            url_list.append(line.rstrip())
    return url_list

if __name__ == '__main__':
    main()
