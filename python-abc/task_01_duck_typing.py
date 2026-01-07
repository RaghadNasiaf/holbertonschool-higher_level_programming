#!/usr/bin/env python3
"""
This module defines an abstract class Shape and demonstrates duck typing.
Classes: Shape, Circle, Rectangle.
Function: shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class for geometric shapes.
    Requires implementation of area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    """

    def __init__(self, radius):
        """Initializes Circle with a radius."""
        self.radius = radius

    def area(self):
        """Implementation of area for Circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Implementation of perimeter for Circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Implementation of area for Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Implementation of perimeter for Rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function that uses Duck Typing to print shape details.
    Does not use isinstance checks.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
