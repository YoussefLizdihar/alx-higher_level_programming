#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """func that reads a text file"""
    with open('filename', 'r') as file:
        content = file.read()
        print(content)
