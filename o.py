from abc import ABC, abstractmethod

# o.py
# The following program was made to demonstrate OCP or 'Open-Closed Principle)
# This principle states that classes, functions, etc should be open for extending, but closed for modification.
# Existing code should not be changed when adding a new functionality.
# The benefit is in reducing the amount of bugs that appear in the code.
# Shape class is open for further additions of new shapes without modifying exist code. 
class Shape(ABC):
    # Abstract base class which defines the method 'get_area()'
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    # Subclass of abstract base class 'Shape' made to implement get_area method.
    # We first initialize
    def __init__ (self, radius):
        self.radius = radius
        pass

    def get_area(self):
        return (3.14 * (self.radius ** 2)) # Formula for calculating area of a circle.

class Square(Shape):
    # Subclass of abstract base class 'Shape' made to implement get_area method.
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (self.side_length ** 2) # Formula for calculating area of a square.
    

class Rectangle(Shape):
    # Subclass of abstract base class 'Shape' made to implement get_area method.
    def __init__ (self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) # Formula for calculating area of a rectangle.


def main():

    # Assign variables with data
    # Print that data to test functionality
    circle = Circle(3)
    print(circle.get_area())
    square = Square(2)
    print(square.get_area())
    rectangle = Rectangle(5, 4)
    print(rectangle.get_area())


if __name__=="__main__":
    main()