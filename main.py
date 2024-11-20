import graph
from scraper import EbayScraper
from server import OllamaServer, count_sentiments_list

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
    reviews_dict = dict_from_file(products, 'reviews')
    #sentiments_dict = produce_sentiments(server, 'phi3:mini', reviews_dict, products)
    sentiments_dict = dict_from_file(products, 'sentiments')
    data_dict = organize_sentiment_data_for_graphing(sentiments_dict, products)
    graph.grouped_bar_chart('Calculus Early Transcendentals (Ebay)', products, data_dict)

def organize_sentiment_data_for_graphing(sentiments_dict, versions):
    new_dict = {
        'Negative' : [],
        'Positive' : [],
        'Neutral' : [],
        }
    for version in versions:
        sentiments = sentiments_dict[version]
        sentiment_count_dict = count_sentiments_list(sentiments)
        new_dict['Negative'].append(sentiment_count_dict['Negative'])
        new_dict['Positive'].append(sentiment_count_dict['Positive'])
        new_dict['Neutral'].append(sentiment_count_dict['Neutral'])
    return new_dict

def scrape_reviews(input_filename, versions):
    review_dict = {}
    # Get urls from input file.
    product_url_list = list_from_file(input_filename)
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

# Saves a list to a file with newlines seperating elements.
def list_to_file(filename, list_to_save):
    with open(filename, 'w') as file:
        for item in list_to_save:
            file.write(item)
            file.write('\n')

# Reads a file as a newline delimited list.
def list_from_file(filename):
    new_list = []
    with open(filename, 'r') as file:
        for line in file:
            new_list.append(line.rstrip())
    return new_list

# Function mainly intended to ease loading 4-5 review/sentiment files into a dictionary.
def dict_from_file(versions, suffix):
    data_dict = {}
    for version in versions:
        data_dict[version] = list_from_file(f"{version} {suffix}.txt")
    return data_dict
    
# Function mainly intended to ease saving 4-5 review/sentiment lists to corresponding files.
def dict_to_file(versions, suffix):
    data_dict = {}
    for version in versions:
        data_dict[version] = list_to_file(f"{version} {suffix}.txt")
    return data_dict
 
if __name__ == '__main__':
    main()
