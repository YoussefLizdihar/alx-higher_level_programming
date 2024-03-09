#!/usr/bin/python3
"""this is a square"""


class Square:
    """private instance attribute"""
    
    def __init__(self, size=0):
        

        #Atr
        self.__size = size
    if Square.__size is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError ("size must be >= 0")
