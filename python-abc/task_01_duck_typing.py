#!/usr/bin/env python3
"""
Module for demonstrating duck typing with shapes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter."""
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Calculate circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
