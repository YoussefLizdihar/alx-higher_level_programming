#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """a class MyList that inherits from list"""
    def __int__(self):
        super().__init__()

    def print_sorted(self):
    print(sorted(self))
