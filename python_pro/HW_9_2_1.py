from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3



circle = Circle(5)
rectangle = Rectangle(3, 4)
triangle = Triangle(5, 12, 13)

figures = [circle, rectangle, triangle]

for figure in figures:
    print(f"Area: {figure.calculate_area()}")
    print(f"Perimeter: {figure.calculate_perimeter()}")
    print()
