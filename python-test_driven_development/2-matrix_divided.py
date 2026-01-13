cat > 2-matrix_divided.py << 'EOF'
#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Each value is rounded to 2 decimal places.
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"
    div_error = "div must be a number"
    zero_error = "division by zero"

    if matrix is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_error)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(matrix_error)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(matrix_error)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError(size_error)

    if not isinstance(div, (int, float)):
        raise TypeError(div_error)

    if div == 0:
        raise ZeroDivisionError(zero_error)

    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(val / div, 2) for val in row] for row in matrix]
EOF

