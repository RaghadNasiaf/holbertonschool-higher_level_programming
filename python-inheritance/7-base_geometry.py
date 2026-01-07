#!/usr/bin/python3
"""
Module 7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry with public instance methods
    """
    def area(self):
        """
        Raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        Args:
            name (str): name of the value
            value (int): value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
