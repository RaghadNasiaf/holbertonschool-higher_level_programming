#!/usr/bin/env python3
"""
This module demonstrates duck typing with geometric shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape with given radius."""
    
    def __init__(self, radius):
        """Initialize a circle with given radius."""
        self.radius = radius
    
    def area(self):
        """Calculate area of circle: π * r²."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate perimeter of circle: 2 * π * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with given width and height."""
    
    def __init__(self, width, height):
        """Initialize a rectangle with given width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area of rectangle: width * height."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter of rectangle: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.
    
    Args:
        shape: An object with area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
