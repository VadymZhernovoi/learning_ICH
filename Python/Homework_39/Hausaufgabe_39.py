"""
1.  Фигуры и площади.
    Создайте абстрактный класс Shape.
    В классе должен быть метод area(), который возвращает площадь фигуры.
    Реализуйте два класса:
    Circle, который принимает радиус.
    Rectangle, который принимает ширину и высоту.

2.  Проверка размеров фигур.
    Доработайте фигуры:
    Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
    Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.
"""
from abc import ABC, abstractmethod


class InvalidSizeError(Exception):
    """ Ошибка когда указан не положительный размер"""

    def __init__(self, side, value):
        self.side = side
        self.value = value
        super().__init__(f"{self.side} ({self.side} = {self.value}) must be positive!")


class Shape(ABC):

    @abstractmethod
    def area(self, *args):
        pass


class Circle(Shape):
    """
     Represents a circle.

     Attributes:
        radius (float): The radius of the rectangle.

     Methods:
        area(): Returns a area of the circle.
    """

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidSizeError("Radius", radius)
        self.radius = radius

    def area(self):
        from math import pi
        return pow(pi * self.radius, 2)


class Rectangle(Shape):
    """
     Represents a rectangle.

     Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

     Methods:
        area(): Returns a area of the rectangle.
     """

    def __init__(self, width: float, height: float):
        if width <= 0:
            raise InvalidSizeError("Width", width)
        if height <= 0:
            raise InvalidSizeError("Height", height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(4.56), Rectangle(3, 5.05)]
for shape in shapes:
    txt = "("
    if hasattr(shape, "radius"):
        txt += f"Radius = {shape.radius}"
    if hasattr(shape, "width"):
        txt += f"Width = {shape.width},"
    if hasattr(shape, "height"):
        txt += f" Height = {shape.height}"
    txt += ")"
    print(f"Area of {shape.__class__.__name__} {txt}: {shape.area():.2f}")

shapes = [Circle(3), Rectangle(3, 5.05)]

try:
    Circle(0)
except InvalidSizeError as e:
    print("Error:", e)
try:
    Rectangle(3, -5.05)
except InvalidSizeError as e:
    print("Error:", e)
