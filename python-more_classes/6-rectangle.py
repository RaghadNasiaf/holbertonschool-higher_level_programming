#!/usr/bin/python3
"""
This module defines a class Rectangle that tracks the number of instances.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns string representation using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for i in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns formal string representation to recreate instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when deleted and decrements instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
