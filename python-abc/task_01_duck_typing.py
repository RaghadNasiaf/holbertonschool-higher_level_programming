#!/usr/bin/env python3
"""
Module for Shape abstract class and its subclasses.
This module demonstrates ABC and Duck Typing concepts.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle, inheriting from Shape.
    """

    def __init__(self, radius: float):
        """
        Initialize the circle with a radius, handling negative values.
        """
        self.radius = abs(radius)

    def area(self) -> float:
        """
        Calculate and return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle, inheriting from Shape.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize the rectangle, handling negative dimensions.
        """
        self.width = abs(width)
        self.height = abs(height)

    def area(self) -> float:
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function that prints area and perimeter using Duck Typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
