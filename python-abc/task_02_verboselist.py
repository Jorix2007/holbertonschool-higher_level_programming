#!/usr/bin/env python3
"""
This module defines the VerboseList class that extends the built-in list class.
It prints notifications upon adding or removing items.
"""

class VerboseList(list):
    """
    A custom list class that provides verbose output when modified.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with an iterable and prints a notification with the 
        number of items added.
        """
        # Calculate the number of items added by comparing length before and after
        # This safely handles generators without throwing a TypeError from len()
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """
        Removes the first occurrence of an item and prints a notification.
        """
        # Edge case handling: verify item exists before printing the message
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns an item at the given index (default is the last item),
        and prints a notification.
        """
        # Retrieve the item first to ensure no IndexError is raised before printing
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
