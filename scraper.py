#!/usr/bin/python
# Scraper.py
#
# Provides classes and functions for scraping review data from a product page.

from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import serialize

# Class representing the basic assumptions of a web scraper for a product page.
class Scraper(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_reviews():
        pass

# A web scraper configured for scraping reviews from Ebay.
class EbayScraper(Scraper):
    # Returns a list containing all reviews for a product.
    def get_reviews(self):
        review_list = []
        # Download the webpage
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
                print('Failed to download initial review webpage')
                raise e
        # Parse it
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if there is more than one page of reviews.
        urls = self.get_page_urls(soup)
        # If the product only has one page of reviews this list will be empty
        # because products with only one page of reviews don't have anything
        # to extract urls from.
        if not urls:
            urls = [self.url]
        # Scrape each page of a product's reviews and add it to the list of strings.
        for url in urls:
            try:
                response = requests.get(url)
            except requests.exceptions.RequestException as e:
                print('Failed to download review webpage')
                raise e
            soup = BeautifulSoup(response.text, 'html.parser')
            review_list.extend(self.get_reviews_from_page(soup))
        return review_list

    # Returns a list of urls to the pages on a multi-page review section.
    # Will return an empty list if the review section is only one page long.
    def get_page_urls(self, soup):
        url_list = []
        # Hyperlinks use a <a> tag.
        for link in soup.find_all('a'):
            # Skip invalid links and any links that don't correspond to page number.
            if not link.get('href') is None and '&pgn=' in link.get('href'):
                # Don't add the same page link twice.
                if not link.get('href') in url_list:
                    url_list.append(link.get('href'))
        return url_list

    # Returns a list of strings where each entry in the list is one review from the page.
    def get_reviews_from_page(self, soup):
        review_list = []
        # Extract only the review text from the entire page.
        for content in soup.find_all('p', itemprop="reviewBody"):
            # Occasionally, the downloaded html document will append 'Read full 
            # review...' to the end of a review despite having the full review
            # already available.
            review_list.append(content.text.replace('Read full review...', ''))
        return review_list

# Returns a dictionary containing the results of running an Ebay scraper on each
# url in the input file.
def scrape_reviews_ebay(input_filename, versions):
    review_dict = {}
    url_list = serialize.list_from_file(input_filename)
    # For each url, version in url_list, versions:
    for i in range(0, len(url_list)):
        scraper = EbayScraper(url_list[i])
        reviews = scraper.get_reviews()
        version = versions[i]
        review_dict[version] = reviews
    return review_dict
