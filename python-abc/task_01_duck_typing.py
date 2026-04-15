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
    