#!/usr/bin/python3
"""
a function that returns the list of available atr and mts of an obj
"""


def lookup(obj):
    """a fct that returns the list of available atr and mts of an obj"""
    return dir(obj)
