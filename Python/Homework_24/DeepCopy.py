'''
Реализуйте аналог deepcopy() с помощью рекурсии. Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
Данные:
original_data = [
 [1, 2, 3], # Вложенный список
 (4, [5, 6], {7, 8}), # Кортеж с вложенными
структурами
 {"a": 9, "b": [10, 11]}, # Словарь со списком
 "Hello", # Строка
 [12, (13, 14)], # Список с кортежем
 15.5, # Число с плавающей точкой
 5 # Целое число
]
'''
from copy import deepcopy

original_data = [
 [1, 2, 3], # Вложенный список
 (4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
 {"a": 9, "b": [10, 11]}, # Словарь со списком
 "Hello", # Строка
 [12, (13, 14)], # Список с кортежем
 15.5, # Число с плавающей точкой
 5 # Целое число
]
def my_deep_copy(items: any) -> list():
    #print(items)
    if isinstance(items, list | set | tuple | dict):
        if isinstance(items, list | set | tuple):
            new_data = list()
            for item in items:
                new_data.append(my_deep_copy(item))
            if isinstance(items, set):
                new_data = set(new_data)
            elif isinstance(items, tuple):
                new_data = tuple(new_data)
        else:
            new_data = dict()
            for key, value in items.items():
                new_data[key] = my_deep_copy(value)
        return new_data
    else:
        return items
    return new_data

print('        original_data:', original_data)
new_data = my_deep_copy(original_data)
print('             new_data:', new_data)
new_data[1][1].append({1,2,3})
new_data[2]["b"] = [12, 13, 14, 15]
print('     changed new_data:', new_data)
print('        original_data:', original_data)
# print()
# original_data = [
#     [1, 2, 3],  # Вложенный список
#     (4, [5, 6], {7, 8}),  # Кортеж с вложенными структурами
#     {"a": 9, "b": [10, 11]},  # Словарь со списком
#     "Hello",  # Строка
#     [12, (13, 14)],  # Список с кортежем
#     15.5,  # Число с плавающей точкой
#     5  # Целое число
# ]
# deepcopy_data = deepcopy(original_data)
# print('        deepcopy_data:', deepcopy_data)
# deepcopy_data[1][1].append({1,2,3})
# print('changed deepcopy_data:', deepcopy_data)
# print('        original_data:', original_data)