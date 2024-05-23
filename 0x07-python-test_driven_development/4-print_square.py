#!/usr/bin/python3
"""
This is the print_square module.
The print_square module supplies one function
this function will take size as an arg
"""


def print_square(size):
    """print the square using "#" with the given size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
