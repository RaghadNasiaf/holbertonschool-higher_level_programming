#!/usr/bin/python3
"""Module 5-square: Printing a square."""


class Square:
    """Class Square that prints."""
    def __init__(self, size=0):
        """Initialize."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return self.__size * self.__size

    def my_print(self):
        """Print square with #."""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
