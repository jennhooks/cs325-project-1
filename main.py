#!/usr/bin/python
# Main.py
# 
# Holds the main function of the program.

import requests

def main():
    # Read the input file as a list of prompts.
    prompts = []
    # Open the file
    input_filename = 'input.txt'
    with open(input_filename, 'r') as file:
        # Strip whitespace from end of line before saving them into list.
        for line in file:
            prompts.append(line.rstrip())

    output_filename = 'output.txt'
    with open(output_filename, 'w') as file:
        for prompt in prompts:
            try:
                response = send_prompt(prompt)
                file.write(response)
                file.write('\n')
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
