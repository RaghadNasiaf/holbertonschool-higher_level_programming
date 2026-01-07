#!/usr/bin/env python3
"""
Module for Task 1: Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

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
        """Init with radius."""
        self.radius = radius

    def area(self):
        """Circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        """Init with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
