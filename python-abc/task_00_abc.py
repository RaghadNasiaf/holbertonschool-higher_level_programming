#!/usr/bin/env python3
"""
This module contains the Animal abstract class and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Implementation of the sound method for Dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Implementation of the sound method for Cat.
        """
        return "Meow"

