#!/usr/bin/env python3
"""
Module for Task 2: Extending the Python List with Notifications.
"""


class VerboseList(list):
    """
    VerboseList class that extends the built-in list class.
    Prints a message for every add or remove operation.
    """

    def append(self, item):
        """Adds an item and prints notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints count of items added."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints notification then removes the item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification then pops the item at the index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
