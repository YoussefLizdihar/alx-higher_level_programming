#!/usr/bin/python3
"""this is a square"""


class Square:
    """private instance attribute"""
    
    def __init__(self, size):
        """Initializes a square with a given size.
        
        Args:
            size: The size of the square.

        """
        self.__size = size
