#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Each element is rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.
    Returns:
        A new matrix with the results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    # Validate that each row is a list and contains only numbers
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # Validate row sizes
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Division logic (handles inf correctly returning 0.0)
    return [[round(x / div, 2) for x in row] for row in matrix]
