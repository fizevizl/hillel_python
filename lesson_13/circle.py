
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return True

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'

class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'Circle({self.x}, {self.y}, R={self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        return Circle(self.radius + other.radius, new.x, new.y)

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        new_radius = abs(self.radius - other.radius)
        if new_radius == 0:
            return Point(self.x, self.y)
        return Circle(new_radius, self.x, self.y)

x = Point(1, 2)
print(x)
a = Circle(5, 5, 7)
b = Circle(5, 1)
print(a, type(a))
c = a + b
print(c, type(c))
d = a - b
print(d, type(d))
