#!/usr/bin/python3

"""
Module composed by a function that multiplies 2 matrices
"""


import numpy as np



def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If the matrices cannot be multiplied.
    """
    # Validate input matrices
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a) == 0 or len(m_a[0]) == 0 or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_a and m_b cannot be empty")

    # Perform matrix multiplication using NumPy
    try:
        result = np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

    return result.tolist()

