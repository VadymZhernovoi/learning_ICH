"""
1.  Среднее время выполнения.
    Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
    Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.
Пример применения:
@measure time
def compute():
    total = 0
    for i in range(10_000_000):
        total += 1
    return total
Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000
"""
from functools import wraps
from time import time

def measure_time(func):
    """
    Декоратор:
    ° запускает функцию 5 раз
    ° считает среднее время выполнения и выводит его на экран
    ° возвращает результат последнего вызова функции.
    :param func:
    :return: результат последнего вызова функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        repeat = 5
        runtime = 0
        for _ in range(repeat):
            start = time()
            result = func(*args, **kwargs)
            runtime += time() - start
        avg = runtime / repeat
        print(f"Среднее время выполнения для {repeat} вызовов: {avg:.2f}")

        return result

    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i

    return total

res = compute()
print(f"Результат: {res}")

"""
2.  Среднее время выполнения с количеством вызовов
    Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
    Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.
Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += 1
    return total
Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000
"""
print()

def measure_time(repeat: int=10):
    """
    Декоратор-фабрика:
    ° принимает число повторов (по умолчанию 5)
    ° запускает функцию указанное количество раз
    ° считает среднее время выполнения
    ° выводит его на экран
    ° возвращает результат последнего вызова.
    :param repeat:
    :return: результат последнего вызова функции
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            runtime = 0
            for _ in range(repeat):
                start = time()
                result = func(*args, **kwargs)
                runtime += time() - start
            avg = runtime / repeat
            print(f"Среднее время выполнения для {repeat} вызовов: {avg:.2f}")

            return result

        return wrapper

    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

res = compute()
print(f"Результат: {res}")
