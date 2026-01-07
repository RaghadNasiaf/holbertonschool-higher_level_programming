#!/usr/bin/env python3
"""
Module for Task 1: Demonstrating duck typing with Shape, Circle, and Rectangle.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Requires implementation of area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Returns circle area: pi * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns circle perimeter: 2 * pi * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns rectangle area: width * height."""
        return float(self.width * self.height)

    def perimeter(self):
        """Returns rectangle perimeter: 2 * (width + height)."""
        return float(2 * (self.width + self.height))


def shape_info(shape):
    """
    Prints area and perimeter of a shape using duck typing.
    Does not use isinstance checks.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
