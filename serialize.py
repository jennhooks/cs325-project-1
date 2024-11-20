#!/usr/bin/python
# Serialize.py
#
# Functions to make I/O for this project slightly easier.

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
