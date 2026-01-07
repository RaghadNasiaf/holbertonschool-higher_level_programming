#!/usr/bin/env python3
"""
Module defining an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Base Class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass representing a Dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a Cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
