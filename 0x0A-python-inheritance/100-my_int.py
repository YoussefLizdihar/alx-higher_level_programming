#!/usr/bin/python3
"""
Write a class MyInt that inherits from int
"""


class MyInt(int):
    """MyInt that inherits from int"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
