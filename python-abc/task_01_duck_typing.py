#!/usr/bin/env python3
"""
Module for demonstrating duck typing with shapes.
This module defines abstract Shape class and concrete Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    All shapes must implement area() and perimeter() methods.
    """
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle shape with given radius.
    """
    
    def __init__(self, radius):
        """
        Initialize a circle.
        
        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate area of circle.
        
        Returns:
            float: Area = π * radius²
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate perimeter (circumference) of circle.
        
        Returns:
            float: Perimeter = 2 * π * radius
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape with given width and height.
    """
    
    def __init__(self, width, height):
        """
        Initialize a rectangle.
        
        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate area of rectangle.
        
        Returns:
            float: Area = width * height
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate perimeter of rectangle.
        
        Returns:
            float: Perimeter = 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.
    
    This function works with any object that has area() and perimeter() methods,
    following the duck typing principle.
    
    Args:
        shape: Object with area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
