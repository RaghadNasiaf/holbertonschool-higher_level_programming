#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
This is part of the Holberton Python OOP project.
"""


class Square:
    """
    Represents a square object.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
