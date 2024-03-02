from abc import ABC, abstractmethod
import math

# l.py
# The following program was made to demonstrate LSP or the Liskov Substitution Principle
# This principle states that a base class can be replaced with a derived class without affecting program functionality.
# ^^^ ("If" the program is using a base class)
# Any derived classes should be replaceable without causing issues. 
# Here, abstract base class called 'Shape' defines get_area() method.
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


# Here, abstract base class called 'HasWidthHeight' defines set_wdith and set_height methods.
# Following methods will eventually be overtwritten by Triangle and Rectangle classes.
class HasWidthHeight(ABC):
    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

class Circle(Shape):
    # Circle class, which is a subclass of Shape, overrides get_area method, utilizing own implementations
    def __init__(self, radius):
        self.radius = radius
    
    def set_radius(self, radius):
        self.radius = radius

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

    def get_area(self):
        return (3.14 * (self.radius ** 2)) # Formula for calculating area of a circle.

class Rectangle(Shape, HasWidthHeight):
    # Rectangle class, which is a subclass of both Shape and HasWidthheight, overrides get_area, set_width, and set_height methods.
    # Utilizes its own implementations
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height) # Formula for calculating area of a rectangle
    

class Triangle(Shape, HasWidthHeight):
    # Triangle class, which is a subclass of both Shape and HasWidthheight, overrides get_area, set_width, and set_height methods.
    # Utilizes its own implementations
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (0.5 * self.width * self.height) # Formula for calculating area of a triangle
    

class Polygon(Shape):
    # Polygon class, which is a subclass of Shape, overrides get_area method, utilizing own implementations
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def get_area(self):
        return (self.num_sides * (self.side_length ** 2)) / (4 * math.tan(math.pi / self.num_sides)) # Formula for calculating area of Polygon


def main():
    
    # Assigning variables to data
    circle = Circle(3)
    # Printing to test functionality
    print(circle.get_area())
    rectangle = Rectangle(5, 4)
    print(rectangle.get_area())
    triangle = Triangle(5, 4)
    print(triangle.get_area())
    polygon = Polygon(3, 3)
    print(polygon.get_area())

if __name__=="__main__":
    main()