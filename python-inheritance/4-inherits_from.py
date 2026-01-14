#!/usr/bin/python3
"""
This module provides a function to check if an object is an inherited
instance of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an inherited instance and not the class itself,
              else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
