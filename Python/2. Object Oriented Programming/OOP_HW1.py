# ```Problem 2: Shape Calculator
# Task:
# Design a system that calculates the area and perimeter of different shapes (Circle, Rectangle, Square). Use polymorphism to achieve this by having a common interface for the calculation methods.

# Steps:
# Create an abstract base class Shape with methods area() and perimeter() that derived classes will override.
# Implement derived classes Circle, Rectangle, and Square that override these methods.
# Use encapsulation to protect the attributes.
# Optionally, implement a method to display information about the shapes.```

class Shapes():
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
        area = (3.14 * int(radius))*(3.14*int(radius))
        perimeter = 2 * 3.14 * radius
        super().__init__(area,perimeter)

class Rectangle(Shapes):
    def __init__ (self, length, width):
        self.lenth = length
        self.width = width
        area = length * width
        perimeter = 2*length + 2*width
        super().__init__(area,perimeter)

class Square(Shapes):
    def __init__(self,side):
        self.side = side
        area = side * side
        perimeter = 4*side
        super().__init__(area,perimeter)


my_circle = Circle(2)
my_rectangle = Rectangle(3,4)
my_square = Square(5)

print(my_circle.area)
print(my_square.area)
print(my_rectangle.area)