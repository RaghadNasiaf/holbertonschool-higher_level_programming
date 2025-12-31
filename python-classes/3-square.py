#!/usr/bin/python3
"""Module 3-square: Square with area method."""


class Square:
    """Square class with area calculation."""
    def __init__(self, size=0):
        """Initialize."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area."""
        return self.__size * self.__size
