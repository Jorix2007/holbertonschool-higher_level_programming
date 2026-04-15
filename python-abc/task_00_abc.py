#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and two subclasses: Dog and Cat.
It demonstrates the use of Python's abc module to enforce method implementation.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing a generic Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Returns the sound of the animal.
        """
        pass

class Dog(Animal):
    """
    Dog subclass that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"

class Cat(Animal):
    """
    Cat subclass that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
    