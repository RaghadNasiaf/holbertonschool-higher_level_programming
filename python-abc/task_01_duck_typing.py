#!/usr/bin/env python3
"""
Module for Task 1: Shapes, Interfaces, and Duck Typing.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area as float."""
        return float(self.width * self.height)

    def perimeter(self):
        """Return rectangle perimeter as float."""
        return float(2 * (self.width + self.height))


def shape_info(shape):
    """Print shape info using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
