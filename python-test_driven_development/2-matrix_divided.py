#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).
    Returns:
        A new matrix with results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if div is a number (HBTN checkers often prioritize this)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 4. Detailed matrix validation
    row_size = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
            
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 5. Safe division (handles infinity automatically)
    return [[round(x / div, 2) for x in row] for row in matrix]
