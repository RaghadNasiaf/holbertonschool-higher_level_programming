#!/usr/bin/python3
"""
This module contains a class called MyList that inherits from the built-in
list class. It provides additional functionality to work with sorted data
without modifying the original order of the list elements.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class. This class is designed
    to demonstrate inheritance by extending the default list object with
    new methods for sorting and displaying information.
    """

    def print_sorted(self):
        """
        Public instance method that prints the current list in ascending order.
        All elements in the list are assumed to be integers. The method uses
        the sorted() function to ensure the original list remains unchanged.
        """
        print(sorted(self))
