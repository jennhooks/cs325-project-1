#!/usr/bin/python
# Server.py
#
# Defines classes representing servers that can run LLMs, recieve prompts,
# and return responses.

from enum import Enum
from abc import ABC, abstractmethod
import requests

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
