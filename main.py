#!/usr/bin/python
# Main.py
#
#
import graph
import serialize
from scraper import EbayScraper
from server import OllamaServer

def main():
    products = [
            '5th edition',
            '6th edition',
            '7th edition',
            '8th edition',
            ]
    # Ollama server running on localhost with default port.
    server = OllamaServer('127.0.0.1', '11434')
    #reviews_dict = scrape_reviews('input.txt', products)
    reviews_dict = serialize.dict_from_file(products, 'reviews')
    #sentiments_dict = produce_sentiments(server, 'phi3:mini', reviews_dict, products)
    sentiments_dict = serialize.dict_from_file(products, 'sentiments')
    data_dict = graph.organize_sentiment_data(sentiments_dict, products)
    graph.grouped_bar_chart('Calculus Early Transcendentals (Ebay)', products, data_dict)

def scrape_reviews(input_filename, versions):
    review_dict = {}
    # Get urls from input file.
    product_url_list = serialize.list_from_file(input_filename)
    # Associate the urls with the dictionary.
    product_dict = {}
    for i in range(0, len(product_url_list)):
        product_dict[product_url_list[i]] = versions[i]
    # For every product scrape the reviews and save them to the dictionary.
    for product in product_dict:
        scraper = EbayScraper(product)
        all_reviews = scraper.get_reviews()
        review_dict[product] = all_reviews
    return review_dict

def produce_sentiments(server, model, review_dict, versions):
    sentiments_dict = {}
    for version in versions:
        reviews = review_dict[version]
        sentiments = server.get_sentiments_list(model, reviews)
        sentiments_dict[version] = sentiments
    return sentiments_dict

if __name__ == '__main__':
    main()
