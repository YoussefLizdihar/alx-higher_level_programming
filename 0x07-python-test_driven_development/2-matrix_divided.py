#!/usr/bin/python3

"""
this module divides a matrix of floats and ints by a div.

Args:
    matrix: a list of rows with floats and ints.
    dix: the divisor.
"""

def matrix_divided(matrix, div):
    """
    this is a method that takes two args, matrix and div.
    it divise the matrix by div.
    """

    #check if the matrix a list of lists of integers or floats
    if all not(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if all rows in the matrix are the same lenght
    if all not(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    #check if the divisor is an int or a float number
    if not(isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    #check if the divisor is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
