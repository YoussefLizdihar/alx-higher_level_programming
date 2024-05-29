#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
using a JSON representation
must use the with statement
"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        content = json.load(file)
        return content
