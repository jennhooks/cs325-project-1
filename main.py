#!/usr/bin/python
# Main.py
# 
# Reads prompts from a text file called input.txt, sends the prompts to
# Phi3-mini and saves the responses to a file called output.txt.

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
    # Open the output file for writing.
    output_filename = 'output.txt'
    with open(output_filename, 'w') as file:
        # Send all prompts.
        for prompt in prompts:
            try:
                # Send prompt and store result in output file.
                response = send_prompt(prompt)
                file.write(response)
                file.write('\n')
            # Catch any errors when sending prompts.
            except requests.exceptions.RequestException:
                print('Failed to send prompt')

# Sends a prompt string to Phi3 mini and returns the response string.
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
