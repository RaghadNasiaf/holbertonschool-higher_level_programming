#!/usr/bin/python3
"""
This module provides a class that inherits from the list type.
The purpose of this module is to demonstrate basic inheritance
concepts by extending the built-in list functionality with a
custom method that prints the list in a sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    It inherits all attributes and methods from the list class
    and adds a specific functionality to print elements sorted.
    """

    def print_sorted(self):
        """
        Public instance method that prints the current list instance
        but in an ascending sorted order. This method assumes that
        all the elements of the list will be of type integer.
        The original list instance is not modified by this method.
        """
        print(sorted(self))
