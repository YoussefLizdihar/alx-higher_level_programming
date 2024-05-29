#!/usr/bin/python3
"""
a function that returns the JSON
representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """func that returns the JSON repr"""
    content = json.dumps(my_obj)
    return content
