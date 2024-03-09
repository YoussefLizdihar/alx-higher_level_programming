#!/usr/bin/python3
"""this is a square"""


class Square:
    """private instance attribute"""

    def __init__(self, size=0):

        # Atr
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
