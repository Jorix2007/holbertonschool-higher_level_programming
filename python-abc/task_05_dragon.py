#!/usr/bin/env python3
"""
This module demonstrates the use of Mixins in Python by composing
behaviors into a Dragon class.
"""

class SwimMixin:
    """
    A mixin that provides swimming capability.
    """

    def swim(self):
        """Prints the swimming behavior."""
        print("The creature swims!")

class FlyMixin:
    """
    A mixin that provides flying capability.
    """

    def fly(self):
        """Prints the flying behavior."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon, inheriting behaviors from 
    both SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints the roaring behavior of the dragon."""
        print("The dragon roars!")
