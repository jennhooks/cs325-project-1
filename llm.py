#!/usr/bin/python
# LLM.py
# 
# Provides a class that represents a LLM running on a specific server and
# provides methods to send prompts to the LLM and recieve responses.

from enum import Enum
import requests

# List of supported servers.
class Servers(Enum):
    OLLAMA = 1

class UnknownServerException(Exception):
    pass

# Class representing an instance of a LLM running on a specific server.
class LanguageModel:
    def __init__(self, model, server):
        self.model = model
        self.server = server

    # Sends the prompt string to the LLM and returns the response.
    def send_prompt(self, prompt):
        # Support for the Ollama server.
        if self.server == Servers.OLLAMA:
            # API url for locally hosted Ollama server.
            url = 'http://localhost:11434/api/generate'
            # Format the request using JSON.
            json_data = {
                    'model': self.model,
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
        # Don't send a prompt if the server is not supported.
        else:
            raise UnknownServerException('The provided server is either unsupported or was not recognized.')
