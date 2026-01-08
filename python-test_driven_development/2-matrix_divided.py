#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Each element is rounded to two decimal places.
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

    # 2. Check if each row is a list and each element is a number
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 3. Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 4. Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Perform division and round to 2 decimal places
    return [[round(x / div, 2) for x in row] for row in matrix]
