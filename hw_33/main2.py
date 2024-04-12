from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        ...

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

    def get_perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    circle = Circle(2)
    print(f"Rectangle area: {rectangle.get_area()}")  # Вывод: Rectangle area: 15
    print(f"Rectangle perimeter: {rectangle.get_perimeter()}")  # Вывод: Rectangle perimeter: 16
    print(f"Circle area: {circle.get_area()}")  # Вывод: Circle area: 12.566370614359172
    print(f"Circle perimeter: {circle.get_perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172


