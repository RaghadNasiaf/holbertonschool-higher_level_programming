#!/usr/bin/env python3
"""Module for Task 1: Shapes and Duck Typing."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # نتركها عملية حسابية عادية لتعطي 28 وليس 28.0
        return self.width * self.height

    def perimeter(self):
        # نتركها عملية حسابية عادية لتعطي 22 وليس 22.0
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
