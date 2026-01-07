#!/usr/bin/env python3
"""
Module for Task 4: Exploring Multiple Inheritance with FlyingFish.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    Demonstrates multiple inheritance and MRO.
    """

    def fly(self):
        """Override fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method."""
        print("The flying fish lives both in water and the sky!")
