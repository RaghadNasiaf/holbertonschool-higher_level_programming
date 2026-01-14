#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class used to represent geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        This is intended to be implemented by subclasses.

        Raises:
            Exception: always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
