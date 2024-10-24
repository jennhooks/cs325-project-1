#!/usr/bin/python
# Scraper.py
#
# Python program that scrapes all reviews associated with several urls and
# stores them in corresponding output files.

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
    # For every product scrape the reviews and save them to a file.
    for product in product_dict:
        all_reviews = get_all_reviews(product)
        save_reviews(all_reviews, product_dict[product])

# Saves the list of review strings to a file named 'PREFIX reviews.txt'
def save_reviews(reviews, file_prefix):
    output_filename = file_prefix + ' reviews'
    with open(output_filename, 'w') as file:
        for review in reviews:
            file.write(review)
            file.write('\n')

# Returns a list containing all reviews for a product.
def get_all_reviews(url):
    review_list = []
    # Download the webpage
    response = requests.get(url)
    # Parse it
    soup = BeautifulSoup(response.text, 'html.parser')
    # Check if there is more than one page of reviews.
    urls = get_review_links(soup)
    # If the product only has one page of reviews this list will be empty
    # because products with only one page of reviews don't have anything
    # to extract urls from.
    if not urls:
        urls = [url]
    # Scrape each page of a product's reviews and add it to the list of strings.
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        review_list.extend(get_reviews(soup))
    return review_list

# Returns a list of strings where each entry in the list is one review from the page.
def get_reviews(soup):
    review_list = []
    # Extract only the review text from the entire page.
    for content in soup.find_all('p', itemprop="reviewBody"):
        # Occasionally, the downloaded html document will append 'Read full 
        # review...' to the end of a review despite having the full review
        # already available.
        review_list.append(content.text.replace('Read full review...', ''))
    return review_list

# Returns a list of urls to the pages on a multi-page review section.
# Will return an empty list if the review section is only one page long.
def get_review_links(soup):
    url_list = []
    # Hyperlinks use a <a> tag.
    for link in soup.find_all('a'):
        # Skip invalid links and any links that don't correspond to page number.
        if not link.get('href') is None and '&pgn=' in link.get('href'):
            # Don't add the same page link twice.
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
