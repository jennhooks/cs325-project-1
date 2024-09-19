#!/usr/bin/python
# Main.py
# 
# Holds the main function of the program.

import requests

def main():
    # Url to the Ollama server hosted on localhost.
    url = 'http://localhost:11434/api/generate'
    # Data to be sent to the server.
    json_data = {
            'model': 'phi3:mini', 
            'prompt': 'Why is the sky blue?',
            'stream': False, # Return only complete responses.
            }
    # Send POST request to server.
    response = requests.post(url, json = json_data)
    # If successful, print the completion.
    if response.status_code == 200:
        print(response.json()['response'])
    # Otherwise, print error.
    else:
        print('POST request failed')

if __name__ == '__main__':
    main()
