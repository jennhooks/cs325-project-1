from scraper import EbayScraper
from server import OllamaServer
import re

def main():
    products = [
            '5th edition',
            '6th edition',
            '7th edition',
            '8th edition',
            ]
    #scrape_reviews('input.txt', products)
    reviews = {}
    for product in products:
        reviews[product] = []
        with open(f"{product} reviews.txt", 'r') as file:
            for line in file:
                reviews[product].append(line.rstrip())
    # Ollama server running on localhost with default port.
    server = OllamaServer('127.0.0.1', '11434')

    for product in products:
        sentiments = generate_sentiments(server, 'phi3:mini', reviews[product])
        sentiments_trimmed = []
        for sentiment in sentiments:
            result = determine_sentiment(sentiment)
            sentiments_trimmed.append(result)
        list_to_file(f"{product} sentiments.txt", sentiments_trimmed)

def scrape_reviews(input_filename, versions):
    review_dict = {}
    # Get urls from input file.
    product_url_list = list_from_file(input_filename)
    # Associate the urls with the output file names.
    product_dict = {}
    for i in range(0, len(product_url_list)):
        product_dict[product_url_list[i]] = versions[i]
    # For every product scrape the reviews and save them to a file.
    for product in product_dict:
        scraper = EbayScraper(product)
        all_reviews = scraper.get_reviews()
        review_dict[product] = all_reviews
    return review_dict

# Asks a LLM whether a set of reviews is positive, negative, or neutral and
# returns the full responses as a list of strings.
def generate_sentiments(server, model, reviews):
    sentiments = []
    for review in reviews:
        response = server.send_prompt(
                model, 
                f'Please tell me whether this comment "{review}" is positive, negative, or neutral?')
        sentiments.append(response)
    return sentiments

# Counts the number of occurences of the words positive, negative, and 
# neutral and assume the word with the most occurences is the correct 
# sentiment.
def determine_sentiment(response):
    counts = {}
    counts['positive'] = len(re.findall('positive', response))
    counts['negative'] = len(re.findall('negative', response))
    counts['neutral'] = len(re.findall('neutral', response))
    return max(counts, key=counts.get)


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
    
if __name__ == '__main__':
    main()
