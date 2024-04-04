class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_area(self):
        return f'area = {self.width * self.height}'


rectangle = Rectangle(14, 14)
print(rectangle.calculate_area())