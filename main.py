#!/usr/bin/python
# Main.py
#
# Produces a chart based on LLM analysis of web scraped reviews from Ebay.
import graph
import serialize
import argparse
from scraper import scrape_reviews_ebay
from server import OllamaServer

def main():
    # Names of the versions of the products.
    products = [
            '5th edition',
            '6th edition',
            '7th edition',
            '8th edition',
            ]
    graph_title = 'Calculus Early Transcendentals (Ebay)'
    # Default host, port, and model to use unless the user overrides this.
    host = '127.0.0.1'
    port = '11434'
    model = 'phi3:mini'

    # Set up argument parsing
    parser = argparse.ArgumentParser(prog='main')
    parser.add_argument('--host', dest='host', type=str, help='Specify a host other than the default (localhost)')
    parser.add_argument('--port', dest='port', type=str, help='Specify a port other than the default (11434)')
    parser.add_argument('--model', dest='model', type=str, help='Specify an alternate LLM to use (default is Phi-3 mini)')
    group = parser.add_argument_group('mode', 'Restricts what computations are performed when running.')
    modes = group.add_mutually_exclusive_group(required=False)
    modes.add_argument('--use-cache', action='store_true', help='Generate a chart using only the saved sentiment files. No scraping or LLM communication is performed.')
    modes.add_argument('--scrape-only', action='store_true', help="Don't generate a chart or sentiments, only update the review files.")
    modes.add_argument('--sentiments-only', action='store_true', help="Don't generate a chart or scrape anything, only update sentiment files based on the current review files.")
    args = parser.parse_args()

    # Check for user overrides.
    if args.host is not None:
        host = args.host
    if args.port is not None:
        port = args.port
    if args.model is not None:
        model = args.model
    # Create the server interface.
    server = OllamaServer(host, port)

    # Only generate chart.
    if args.use_cache:
        sentiments_dict = serialize.dict_from_file(products, 'sentiments')
        data_dict = graph.organize_sentiment_data(sentiments_dict, products)
        graph.grouped_bar_chart('Calculus Early Transcendentals (Ebay)', products, data_dict)
    # Only generate review files.
    elif args.scrape_only:
        reviews_dict = scrape_reviews_ebay('input.txt', products)
        serialize.dict_to_file(products, reviews_dict, 'reviews')
    # Only generate sentiment files based on existing review files.
    elif args.sentiments_only:
        reviews_dict = serialize.dict_from_file(products, 'reviews')
        sentiments_dict = server.reviews_to_sentiments(model, reviews_dict, products)
        serialize.dict_to_file(products, sentiments_dict, 'sentiments')
    # Run everything
    else:
        reviews_dict = scrape_reviews_ebay('input.txt', products)
        serialize.dict_to_file(products, reviews_dict, 'reviews')
        sentiments_dict = server.reviews_to_sentiments(model, reviews_dict, products)
        serialize.dict_to_file(products, sentiments_dict, 'sentiments')
        data_dict = graph.organize_sentiment_data(sentiments_dict, products)
        graph.grouped_bar_chart(graph_title, products, data_dict)

if __name__ == '__main__':
    main()
