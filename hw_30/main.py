class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


    def __str__(self):
        return f'Rectangle area = {self.area()}.'


    def __repr__(self):
        return f'Rectangle perimeter = {self.perimeter()}.'


rectangle = Rectangle(23, 12)
print(rectangle, rectangle.__repr__(), sep='\n')