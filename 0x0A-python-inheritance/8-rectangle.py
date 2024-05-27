#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """BaseGeometry Class (from 7-base_geometry.py)"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
