"""
1.  Класс Rectangle
    Создайте класс Rectangle, который описывает прямоугольник.
    У каждого объекта должны быть два поля: width и height.
    Добавьте метод get_area(), который возвращает площадь прямоугольника.
    Создайте объект прямоугольника с произвольными значениями.
    Выведите его площадь.
    Измените ширину и высоту.
    Выведите новую площадь.
Пример вывода:
Площадь: 20
Новая площадь: 35
"""


class Rectangle:
    """ Создаёт объект прямоугольник с двумя атрибутами: высота и ширина """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


rect = Rectangle(4, 5)
print("Площадь:", rect.get_area())

rect.width = 5
rect.height = 7
print("Новая площадь:", rect.get_area())

"""
2.  Класс Counter
    Реализуйте класс Counter, который представляет собой простой счётчик.
    Счётчик должен начинаться с нуля.
    Предусмотрите методы для увеличения и уменьшения значения на единицу, при этом при каждой операции должно отображаться новое значение счётчика.
    Добавьте метод, возвращающий текущий результат.
    Проверьте работу счётчика, выполнив несколько операций.
Пример вывода:
Значение увеличено, текущее: 1
Значение увеличено, текущее: 2
Значение увеличено, текущее: 3
Значение уменьшено, текущее: 2
Текущее значение: 2
"""
print()


# не совсем понял когда должен печататься результат, поэтому сделал два варианта

class Counter1:
    """ Создаёт объект простой счётчик. Счётчик начинается с нуля."""

    def __init__(self):
        self.cnt = 0

    def set_increment(self):
        self.cnt += 1
        print(f"Значение увеличено, текущее: {self.cnt}")

    def set_decrement(self):
        self.cnt -= 1
        print(f"Значение уменьшено, текущее: {self.cnt}")

    def get_status(self):
        return self.cnt


cnt1 = Counter1()

for _ in range(3):
    cnt1.set_increment()

cnt1.set_decrement()

print("Текущее значение:", cnt1.get_status())

# или так
print()


class Counter2:
    """ Создаёт объект простой счётчик. Счётчик начинается с нуля."""

    def __init__(self):
        self.cnt = 0

    def set_increment(self):
        self.cnt += 1
        return self.cnt

    def set_decrement(self):
        self.cnt -= 1
        return self.cnt

    def get_status(self):
        return self.cnt


cnt2 = Counter2()

for _ in range(3):
    print(f"Значение увеличено, текущее: {cnt2.set_increment()}")

print(f"Значение уменьшено, текущее: {cnt2.set_decrement()}")

print(f"Текущее значение: {cnt2.get_status()}")
