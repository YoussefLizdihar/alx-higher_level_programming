#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
and then save them to a file
"""


import sys
from os.path import exists
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
