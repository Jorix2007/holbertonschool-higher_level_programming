#!/usr/bin/env python3
"""
This module defines an abstract base class Shape, concrete subclasses 
Circle and Rectangle, and a standalone function to demonstrate duck typing.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Concrete subclass representing a Circle.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        Handles negative radius by taking the absolute value.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Concrete subclass representing a Rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with a width and height.
        Handles negative dimensions by taking the absolute value.
        """
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    
    This function relies on the fact that the passed object behaves like
    a Shape (having area() and perimeter() methods) without strictly 
    checking its type.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
