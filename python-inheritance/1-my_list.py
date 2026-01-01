#!/usr/bin/python3
"""
This module provides a specialized class for handling list operations.
The main purpose is to demonstrate inheritance by extending the
standard list data structure with unique sorting capabilities.
"""


class MyList(list):
    """
    MyList is a subclass that expands the built-in list features.
    It provides additional functionality to display elements in a
    specific order while maintaining the integrity of the original data.
    """

    def print_sorted(self):
        """
        Public method that displays the elements in ascending order.
        This procedure ensures that all integer elements are presented
        consistently without modifying the instance itself.
        """
        print(sorted(self))
