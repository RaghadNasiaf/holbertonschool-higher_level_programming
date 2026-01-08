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
        div: A number (integer or float).

    Returns:
        A new matrix containing the results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check divisor type first (Priority for Checker)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check divisor value
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check matrix type and content
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_size = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        
        # Check for consistent row size
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
            
        # Check element types
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 4. Perform division and return new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
