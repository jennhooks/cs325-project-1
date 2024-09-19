#!/usr/bin/python
# Main.py
# 
# Holds the main function of the program.

import requests

def main():
    try:
        response = send_prompt('Why is the sky blue?')
        print(response)

        response = send_prompt('Why is Mars red?')
        print(response)

        response = send_prompt('What is 6 + 4?')
        print(response)
    except requests.exceptions.RequestException:
        print('Failed to send prompt')

def send_prompt(prompt):
    # Url to the Ollama server hosted on localhost.
    url = 'http://localhost:11434/api/generate'
    # Data to be sent to the server.
    json_data = {
            'model': 'phi3:mini', 
            'prompt': prompt,
            'stream': False, # Return only complete responses.
            }
    # Send POST request to server and try to get the response.
    try:
        response = requests.post(url, json = json_data)
        return response.json()['response']
    # If it failed
    except requests.exceptions.RequestException:
        print('POST request failed')
        raise

if __name__ == '__main__':
    main()
