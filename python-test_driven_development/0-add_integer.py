#!/usr/bin/python3
"""
This is a module that provides a specific function for integer addition.
The module is part of a higher-level programming project focused on 
test-driven development practices. It ensures that all inputs are properly 
validated and casted to integers before any arithmetic operation occurs.
"""


def add_integer(a, b=98):
    """
    This function adds two numbers together after validating their types.
    It accepts both integers and floats as inputs, but it will always 
    cast them to integers before performing the final addition.
    If the inputs are not valid numbers, a TypeError will be raised.

    Args:
        a: The first number to be added, must be an integer or a float.
        b: The second number to be added, must be an integer or a float.
    
    Returns:
        The integer result of the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
