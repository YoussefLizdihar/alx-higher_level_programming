#!/usr/bin/python3
"""
a class Student that defines a student by
Public instance attributes and a public method
"""


class Student:
    """class Student defined by:
    first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
