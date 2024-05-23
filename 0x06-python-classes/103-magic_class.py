#!/usr/bin/python3

import math

class MagicClass:
    """A class that represents a circle with methods to calculate its area and circumference."""

    def __init__(self, radius=0):
        """Initializes the MagicClass with a radius."""
        self.__radius = 0  # Initial value for radius

        # Type checking for radius
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        # Assign the radius
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates and returns the circumference of the circle."""
        return (2 * math.pi * self.__radius)
