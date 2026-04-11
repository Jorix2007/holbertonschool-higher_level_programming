#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list elements in ascending sorted order."""
        print(sorted(self))
