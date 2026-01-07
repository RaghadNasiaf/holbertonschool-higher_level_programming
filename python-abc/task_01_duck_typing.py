#!/usr/bin/env python3
"""
This module defines an abstract class Shape and its subclasses Circle
and Rectangle, demonstrating duck typing and abstract base classes.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Base Class for all geometric shapes.
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
    Class representing a circle that inherits from Shape.
    """

    def __init__(self, radius):
        """Initializes the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    
    print("Perimeter: {}".format(shape.perimeter()))
