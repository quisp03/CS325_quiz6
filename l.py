from abc import ABC, abstractmethod
import math

# l.py

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class HasWidthHeight(ABC):
    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def set_radius(self, radius):
        self.radius = radius

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

    def get_area(self):
        return (3.14 * (self.radius ** 2)) # formula for circle area

class Rectangle(Shape, HasWidthHeight):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height) # formula for rectangle area
    

class Triangle(Shape, HasWidthHeight):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (0.5 * self.width * self.height) # formula for triangle area
    

class Polygon(Shape):
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def get_area(self):
        return (self.num_sides * (self.side_length ** 2)) / (4 * math.tan(math.pi / self.num_sides)) # formula for polygon area


def main():
    
    circle = Circle(3)
    print(circle.get_area())
    rectangle = Rectangle(5, 4)
    print(rectangle.get_area())
    triangle = Triangle(5, 4)
    print(triangle.get_area())
    polygon = Polygon(3, 3)
    print(polygon.get_area())

if __name__=="__main__":
    main()