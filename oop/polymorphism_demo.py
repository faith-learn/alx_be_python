# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        #Abstract method to be implemented by subclasses
        raise NotImplementedError("Subclasses must override the area() method.")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Demonstration of polymorphism
if __name__ == "__main__":
    # Create objects of different shapes
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Rectangle(3, 8),
        Circle(2.5)
    ]

    # Each object calls its own area() method
    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")