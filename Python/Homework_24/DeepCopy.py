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

def my_deep_copy(objects: any) -> any:
    '''
    Аналог deepcopy() с помощью рекурсии.
    :param objects: коллекция с любым количеством любой вложенности любых объектов.
    :return: независимая копия коллекции
    '''
    #print(objects)
    if isinstance(objects, list | set | tuple | dict):
        if isinstance(objects, list | set | tuple):
            new_data = list()
            for item in objects:
                new_data.append(my_deep_copy(item))
            if isinstance(objects, set):
                new_data = set(new_data)
            elif isinstance(objects, tuple):
                new_data = tuple(new_data)
        else:
            new_data = dict()
            for key, value in objects.items():
                new_data[key] = my_deep_copy(value)
        return new_data
    else:
        return objects
    return new_data


original_data = [
    [1, 2, 3],  # Вложенный список
    (4, [5, 6], {7, 8}),  # Кортеж с вложенными структурами
    {"a": 9, "b": [10, 11]},  # Словарь со списком
    "Hello",  # Строка
    [12, (13, 14)],  # Список с кортежем
    15.5,  # Число с плавающей точкой
    5  # Целое число
]
print('        original_data:', original_data)
new_data = my_deep_copy(original_data)
print('             new_data:', new_data)
# проверяем
new_data[1][1].append({1,2,3})
new_data[2]["b"] = [12, 13, 14, 15]
new_data[3] = 'DeepCopy'
new_data[4][1] = (111,222,333)
new_data[5] = 9999.123456789
new_data[6] = 12345
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