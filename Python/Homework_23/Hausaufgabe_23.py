'''
1.  Объединение данных в строку
    Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари)
    и возвращает их строковое представление, объединённое через " | ".
    Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
    Данные: data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
    Пример вывода:
    42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
'''
from functools import reduce
from typing import Any

def list_parsed(data: list[Any]) -> str:
    '''
    Функция принимает список любых данных и возвращает их строковое представление, объединённое через " | ".

    :param data: список любых объектов (строки, числа, списки, словари)
    :return: строка с разделителем " | "
    '''
    result = " | ".join(map(str, data))
    #result = reduce(lambda s, o: s + ' | ' + o, map(str, data))

    return result

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(data)
print(list_parsed(data))

'''
2.  Сумма вложенных чисел
    Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов. 
    Функция должна вернуть сумму всех чисел. 
    Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
    Данные:
    data = [
            {"name": "Alice", "scores": [10, 20, 30]},
            {"name": "Bob", "scores": [5, 15, 25]},
            {"name": "Charlie", "scores": [7, 17, 27]}
            ]
    Пример вывода:
    Итоговый балл: 156
'''
def sum_scores(data: list[dict[str,list[int]]]) -> int:
    '''
    Функция принимает список словарей, где каждый словарь содержит имя пользователя и список баллов,
    и возвращает сумму всех чисел.

    :param data: список словарей [{"name": str, "scores": list[int]}]
    :return: cумма всех чисел из списка "scores"
    '''
    if not data:
        return 0
    #result = sum(map(lambda val: sum(val["scores"]), data))
    result = reduce(lambda x, y: x + y, map(lambda s: sum(s["scores"]), data))

    return result

data = [
        {"name": "Alice", "scores": [10, 20, 30]},
        {"name": "Bob", "scores": [5, 15, 25]},
        {"name": "Charlie", "scores": [7, 17, 27]},
    {"name": "Ttt", "scores": []},
        ]
#data = []
print()
print(data)
print("Итоговый балл:", sum_scores(data))
