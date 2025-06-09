"""
Python class methods
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def display_area(self):
        print(f'Area of rectangle: {self.base * self.height} units^2')


new_rectangle = Rectangle(12, 10)

new_rectangle.display_area()
