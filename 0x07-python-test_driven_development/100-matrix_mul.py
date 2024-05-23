#!/usr/bin/python3

"""
Module composed by a function that multiplies 2 matrices

Args:
        m_a (list of lists): The first matrix.                                                                                                                                             m_b (list of lists): The second matrix.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    Returns:
        list of lists: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list of lists,
                   or if elements of m_a or m_b are not integers or floats,
                   or if rows of m_a or m_b are not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b can't be multiplied.
    """
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not all(row for row in m_a):
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    num_columns_a = len(m_a[0])
    num_rows_b = len(m_b)
    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    num_rows_a = len(m_a)
    num_columns_b = len(m_b[0])
    result = [[0 for _ in range(num_columns_b)] for _ in range(num_rows_a)]

    for i in range(num_rows_a):
        for j in range(num_columns_b):
            for k in range(num_columns_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
