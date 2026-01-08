#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Each result is rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix containing the division results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Check if each row is a list and elements are numbers
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 3. Check if each row of the matrix is of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 4. Check divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Perform division and round to 2 decimal places
    return [[round(x / div, 2) for x in row] for row in matrix]
