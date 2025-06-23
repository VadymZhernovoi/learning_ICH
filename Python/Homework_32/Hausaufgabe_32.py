'''
1.  Фабрика функций округления
    Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
    Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))
Пример вывода:
3.14
2.72
10.0
'''
def make_rounder(n_point: int):
    def rounder(number: int):
        return round(number, n_point)
    return rounder

round2 = make_rounder(2)
round0 = make_rounder(0)
round3 = make_rounder(3)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))
print(round3(9.123456))

'''
2.  Расширяемый логгер событий
    Создайте функцию, которая возвращает вложенный логгер событий.
    Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано) и возвращать весь список событий.
Пример вызова: 
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)
Пример вывода: 
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
'''
from datetime import datetime
def logger():
    records = list()
    def set_log(event: str=""):
        if event:
            records.append(f"{event}: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        return records
    return set_log
log = logger()
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

'''
3.  Рамка вокруг вывода
    Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -, 
    выводя по строке до и после вызова функции.
Пример декорируемой функции: 
def say_hello():
    print("Привет, игрок!")
Пример вывода: 
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
'''
def frame(func):
    def wrapper():
        print("-" * 50)
        func()
        print("-" * 50)
    return wrapper
@frame
def say_hello():
    print("Привет, игрок!")

@frame
def say_bay():
    print("Пока, игрок!")

say_hello()
print()
say_bay()
