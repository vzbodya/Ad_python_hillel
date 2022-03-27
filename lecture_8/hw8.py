import math
from colorama import Fore, Style

# 1. Створити frange ітератор. Який буде працювати з float.


class frange:

    def __init__(self, stop_point, start_point=None, step=1.0):
        if start_point is not None:
            self.start = stop_point
            self.stop = start_point
            self.step = step
        else:
            self.stop = stop_point
            self.start = 0
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step < 0:
            if self.start - self.step <= self.stop - self.step:
                raise StopIteration
            value = self.start
            self.start += self.step
            return value

        if self.start + self.step >= self.stop + self.step:
            raise StopIteration

        value = self.start
        self.start += self.step
        return value


for i in frange(1, 100, 3.5):
    print(i)

# 2. Створити context manager який буде фарбувати колір виведеного тексту


class colorized:

    def __init__(self, color="cyan"):
        color = color.upper()
        self.color = Fore.__getattribute__(color)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def print_painted(self, message: str):
        print(f"{self.color}{message}{Style.RESET_ALL}")


with colorized("yellow") as colorizer:
    colorizer.print_painted("Hello, world!")


# 3. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).
#    Triangle - треба створити клас


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle, base):
        super().__init__(x, y, height, width)
        self.angle = angle
        self.base = base

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.base * self.height


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


class Triangle(Parallelogram):
    def __int__(self, x, y, height, width, angle, base):
        super().__init__(x, y, height, width, angle, base)

    def square(self):
        return 0.5 * self.base * self.height


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45, 10)
p1 = Parallelogram(1, 2, 20, 30, 45, 10)
str(p1)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)

print(f"Total square equals to {scene.total_square()}")
