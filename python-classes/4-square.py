#!/usr/bin/python3
"""Module 4-square: Defines Square with property."""


class Square:
    """Class Square with getter and setter."""
    def __init__(self, size=0):
        """Initialize."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return self.__size * self.__size
