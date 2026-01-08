#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
It is a simple implementation for learning TDD.
It includes type validation for integers and floats.
The result is always returned as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers. Floats are casted to ints.
    Raises TypeError if inputs are not numbers.
    Returns the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or abs(a) > 1.7976931348623157e+308:
        raise TypeError("a must be an integer")
    if b != b or abs(b) > 1.7976931348623157e+308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
