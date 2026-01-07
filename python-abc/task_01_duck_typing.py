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
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Calculate area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area as float."""
        return float(self.width * self.height)

    def perimeter(self):
        """Return perimeter as float."""
        return float(2 * (self.width + self.height))


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
