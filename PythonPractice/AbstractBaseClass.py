from abc import ABC, abstractmethod


class Shape(ABC): # ABC Means class is abstract class
    @abstractmethod  # This will force all the subclasses to implement print_area function
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length + self.breadth


rect1 = Rectangle()
print(rect1.print_area())
