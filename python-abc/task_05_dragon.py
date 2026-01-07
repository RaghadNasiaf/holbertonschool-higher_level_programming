#!/usr/bin/env python3
"""
Module for Task 5: Demonstrating Mixins with Dragon, SwimMixin, and FlyMixin.
"""


class SwimMixin:
    """Mixin class to add swimming functionality."""
    def swim(self):
        """Prints a swimming notification."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying functionality."""
    def fly(self):
        """Prints a flying notification."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines behaviors from SwimMixin and FlyMixin.
    Also includes a unique roar method.
    """
    def roar(self):
        """Prints a roar notification."""
        print("The dragon roars!")
