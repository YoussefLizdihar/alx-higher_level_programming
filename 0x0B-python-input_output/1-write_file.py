#!/usr/bin/python3
"""
a function that write a string into a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """func that write a string to a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
        return content 
