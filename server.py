#!/usr/bin/python
# Server.py
#
# Defines classes representing servers that can run LLMs, recieve prompts,
# and return responses.

from enum import Enum
from abc import ABC, abstractmethod
import requests
import re

# Class representing the basic assumptions of a server that can run a LLM.
class Server(ABC):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @abstractmethod
    def send_prompt(self, model, prompt):
        pass

# Class representing a running Ollama server.
class OllamaServer(Server):
    # Sends the prompt string to the LLM and returns the response.
    def send_prompt(self, model, prompt):
        # API url for Ollama server.
        url = f"http://{self.host}:{self.port}/api/generate"
        # Format the request using JSON.
        json_data = {
                'model': model,
                'prompt': prompt,
                'stream': False,
                }
        # Attempt to send the request and return the response if successful.
        try:
            response = requests.post(url, json = json_data)
            return response.json()['response']
        # Catch all request exceptions.
        except requests.exceptions.RequestException as e:
            print('POST request failed')
            raise e

    # Asks a LLM whether individual comments are positive, negative, or 
    # neutral and returns the full responses as a list of strings.
    def generate_sentiments(self, model, comments):
        sentiments = []
        for comment in comments:
            response = self.send_prompt(
                    model, 
                    f'Please tell me whether this comment "{comment}" is positive, negative, or neutral?')
            sentiments.append(response)
        return sentiments

    # Returns a list of one-word sentiment strings when given a list of
    # comments that should be interpreted by the LLM.
    def get_sentiments_list(self, model, comments):
        sentiments = []
        for response in self.generate_sentiments(model, comments):
            sentiments.append(determine_sentiment(response))
        return sentiments


    def reviews_to_sentiments(self, model, review_dict, versions):
        sentiments_dict = {}
        for version in versions:
            reviews = review_dict[version]
            sentiments = self.get_sentiments_list(model, reviews)
            sentiments_dict[version] = sentiments
        return sentiments_dict

# Counts the number of occurences of the words positive, negative, and 
# neutral and assume the word with the most occurences is the correct 
# sentiment.
def determine_sentiment(response):
    counts = {}
    counts['positive'] = len(re.findall('positive', response))
    counts['negative'] = len(re.findall('negative', response))
    counts['neutral'] = len(re.findall('neutral', response))
    return max(counts, key=counts.get)

# Converts the list of one-word sentiment strings into a dictionary
# with seperate counts for each sentiment.
def count_sentiments_list(sentiments):
    sentiment_dict = {
            'Negative' : 0,
            'Positive' : 0,
            'Neutral' : 0,
            }
    for sentiment in sentiments:
        if sentiment == 'positive':
            sentiment_dict['Positive'] += 1
        elif sentiment == 'negative':
            sentiment_dict['Negative'] += 1
        elif sentiment == 'neutral':
            sentiment_dict['Neutral'] += 1

    return sentiment_dict


