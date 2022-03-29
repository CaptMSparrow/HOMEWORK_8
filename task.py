from abc import ABC, abstractclassmethod


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line():
    def __init__(self, x, y):
        Point.__init__(self, x, y)
        # self._len = Point(x, y)
        # self.x = x
        # self.y = y

    def length(self):
        len = (self.x**2 + self.y**2)**0.5
        print(f'lenght = {len}')


class Shape(ABC):
    @property
    @abstractclassmethod
    def area(self):
        pass

    @property
    @abstractclassmethod
    def perimeter(self):
        pass


class Square(Line, Shape):
    def area(self):
        S = self.x ** 2
        print(f'Square area = {S}')

    def perimeter(self):
        P = 4 * self.x
        print(f'Square perimeter = {P}')


class Rect(Shape):
    def __init__(self, x, y):
        self._sp = Line(x, y)

    def length(self):
        length = self._sp.length()

    def area(self):
        S = self._sp.x * self._sp.y
        print(f'Rect area = {S}')

    def perimeter(self):
        P = 2 * (self._sp.x + self._sp.y)
        print(f'Rect perimeter = {P}')


class Cube(Square):
    def volume(self):
        V = self.x ** 3
        print(f'Cube volume = {V}')


p = Cube(3, 4)
p.length()
p.area()
p.perimeter()
p.volume()
