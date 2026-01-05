#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Class MyList inherits from list and adds a sorting print method.
    """

    def print_sorted(self):
        """
        Method that prints the list in ascending sorted order.
        """
        print(sorted(self))
