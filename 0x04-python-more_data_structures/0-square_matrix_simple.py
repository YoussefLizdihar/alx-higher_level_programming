#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        new = list(map(lambda x: x ** 2, row))
        newmatrix.append(new)
    return newmatrix
