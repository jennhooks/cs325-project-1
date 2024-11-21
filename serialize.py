#!/usr/bin/python
# Serialize.py
#
# Functions to make I/O for this project slightly easier.
from pathlib import Path

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
def dict_from_file(prefixes, suffix, path='.'):
    data_dict = {}
    filename = Path(path)
    for prefix in prefixes:
        data_dict[prefix] = list_from_file(filename / f"{prefix} {suffix}.txt")
    return data_dict
    
# Function mainly intended to ease saving 4-5 review/sentiment lists to corresponding files.
def dict_to_file(data_dict, suffix, path='.'):
    filename = Path(path)
    for prefix, data in data_dict.items():
        list_to_file(filename / f"{prefix} {suffix}.txt", data_dict[prefix])
