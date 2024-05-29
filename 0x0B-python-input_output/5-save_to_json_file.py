#!/usr/bin/python3
"""
a function that writes an Object to a text file
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """func that writes an Object using JSON"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
