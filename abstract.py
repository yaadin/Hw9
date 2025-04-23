from abc import ABC, abstractmethod
import math
import random

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    
    def volume(self):
        ...

class Sphere(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
       return 4 * math.pi * self.rad ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.rad ** 3
    
class Cylinder(Shape):
    def __init__(self, rad, height):
        self.rad = rad
        self.height = height

    def area(self):
        return 2 * math.pi * self.rad * (self.rad + self.height)

    def volume(self):
        return math.pi * self.rad ** 2 * self.height


class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

shapes = []
for _ in range(10):
    shape_type = random.choice(["Sphere", "Cylinder", "Cube"])
    if shape_type == "Sphere":
        rad = random.uniform(1, 10)
        shapes.append(Sphere(rad))
    elif shape_type == "Cylinder":
        rad = random.uniform(1, 10)
        height = random.uniform(5, 20)
        shapes.append(Cylinder(rad, height))
    else:
        side = random.uniform(1, 10)
        shapes.append(Cube(side))
    
for shape in shapes:
    print(f"{type(shape).__name__:<10} {shape.area():<20.2f} {shape.volume():<20.2f}")