"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def display_circumference(self):
        return f'Circumference: {2 * self.pi * self.radius} units'

    def display_area(self):
        return f'Area: {self.pi * self.radius**2} square units'


if __name__ == "__main__":

    circle1 = Circle(2)

    print(circle1.display_circumference())
    print(circle1.display_area())
