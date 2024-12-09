# shape base class with an area(method)
# Subslasses such as suare, circle...

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

#Main  
c1 = Circle(7)
print(c1.area())
r1 = Rectangle(4, 5)
print(r1.area())