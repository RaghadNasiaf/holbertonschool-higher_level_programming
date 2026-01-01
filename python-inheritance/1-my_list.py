#!/usr/bin/python3
"""
This module provides a specialized class for list manipulation.
It contains the MyList class which extends the built-in list functionality
by adding a method to display its elements in a sorted fashion.
"""


class MyList(list):
    """
    MyList is a subclass that inherits all features from the Python list.
    This class is intended to demonstrate how inheritance works in Python 3
    by allowing the user to print a sorted version of the list easily.
    """

    def print_sorted(self):
        """
        This method prints the elements of the list in ascending sorted order.
        It assumes that the list only contains integer elements to sort.
        The original list remains unchanged after this operation is performed.
        """
        print(sorted(self))
