#!/usr/bin/python3
"""
This module provides a function that adds two integers together.
The integers can be provided as positive numbers, negative numbers,
or floating point numbers which will be casted to integers.
This project is part of the Test-driven development curriculum.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    The function checks if the inputs are either integers or floats.
    If they are floats, they are converted to integers before addition.
    If the inputs are not valid numbers, a TypeError is raised.
    Args:
        a: The first number to be added.
        b: The second number, which defaults to 98.
    Returns:
        The sum of a and b as an integer value.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
