#!/usr/bin/python3
"""
a class Student that defines a student by
Public instance attributes
"""


class Student:
	"""class Student defined by:
	first_name, last_name, age"""
	
	def __int__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		return self.__dict__
