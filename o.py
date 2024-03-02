from abc import ABC, abstractmethod

# o.py

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
        pass

    def get_area(self):
        return (3.14 * (self.radius ** 2))

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (self.side_length ** 2)
    

class Rectangle(Shape):
    def __init__ (self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height)


def main():
    circle = Circle(3)
    print(circle.get_area())
    square = Square(2)
    print(square.get_area())
    rectangle = Rectangle(5, 4)
    print(rectangle.get_area())


if __name__=="__main__":
    main()