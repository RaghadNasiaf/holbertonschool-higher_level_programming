#!/usr/bin/python3
"""
This module provides a function for integer addition.
The function ensures both arguments are integers or floats.
Floats are casted to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number (int or float)
        b: second number (int or float, default 98)
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
