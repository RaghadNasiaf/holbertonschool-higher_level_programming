#!/usr/bin/env python3
"""
Module for Task 1: Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
