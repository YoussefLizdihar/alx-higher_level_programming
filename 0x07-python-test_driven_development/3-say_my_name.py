#!/usr/bin/python3

"""
this module takes your first and last name
and add them toghather with 'My name is'.

Args:
    first name
    last name
"""


def say_my_name(first_name, last_name=""):
    """this is a method that takes your first name, last name is optional"""
    if not isinstance(first_name), str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
