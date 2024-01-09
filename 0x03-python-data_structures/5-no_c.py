#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for char in my_string:
        if char.lower() != 'c':
            newstring += char
    return newstring
