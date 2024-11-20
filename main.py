def main():
    pass

# Project 1
#def main():
#    # Read the input file as a list of prompts.
#    prompts = []
#    # Open the file
#    input_filename = 'input.txt'
#    with open(input_filename, 'r') as file:
#        # Strip whitespace from end of line before saving them into list.
#        for line in file:
#            prompts.append(line.rstrip())
#    # Open the output file for writing.
#    output_filename = 'output.txt'
#    with open(output_filename, 'w') as file:
#        # Send all prompts.
#        for prompt in prompts:
#            try:
#                # Send prompt and store result in output file.
#                response = send_prompt(prompt)
#                file.write(response)
#                file.write('\n')
#            # Catch any errors when sending prompts.
#            except requests.exceptions.RequestException:
#                print('Failed to send prompt')

# Project 2
#def main():
#    # Get urls from input file.
#    product_url_list = get_product_links()
#    # Define names for the output files.
#    product_versions = ['5th edition', '6th edition', '7th edition', '8th edition']
#    # Associate the urls with the output file names.
#    product_dict = {}
#    for i in range(0, len(product_url_list)):
#        product_dict[product_url_list[i]] = product_versions[i]
#    # For every product scrape the reviews and save them to a file.
#    for product in product_dict:
#        all_reviews = get_all_reviews(product)
#        save_reviews(all_reviews, product_dict[product])

if __name__ == '__main__':
    main()
