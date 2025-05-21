'''
1.  Не уникальные числа
    Напишите программу, которая находит все числа, встречающиеся более одного раза в списке, и выводит их в порядке убывания.
    Данные: numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
    Пример вывода:
    Числа, встречающиеся более одного раза: [7, 4, 3, 8]
'''
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

numbers_uniq = {number for number in numbers if numbers.count(number) > 1}

print('Числа, встречающиеся более одного раза:', sorted(list(numbers_uniq), reverse=True))
# или
for number in numbers:
    if numbers.count(number) > 1 and number not in numbers_uniq:
        numbers_uniq.append(number)
print('Числа, встречающиеся более одного раза:', sorted(numbers_uniq, reverse=True))

'''
2.  Проверка подмножества 
    Напишите программу, которая проверяет, является ли один словарь подмножеством другого 
    (т.е. все его пары "ключ-значение" содержатся в другом словаре).
    Данные: dict1 = {"a": 1, "b": 2}
            dict2 = {"a": 1, "b": 2, "c": 3}
    Пример вывода:
    Первый словарь является подмножеством второго.
'''
dict2 = {"a": 1, "b": 3}
dict1 = {"a": 1, "b": 2, "c": 3}
print()
flag = 0
if len(dict1) < len(dict2):
    flag = 1
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            flag = 0
else:
    flag = 2
    for key in dict2:
        if key not in dict1 or dict2[key] != dict1[key]:
            flag = 0
if flag > 0 and len(dict1) == len(dict2):
    flag = 3

match flag:
    case 1:
        print('Первый словарь является подмножеством второго.')
    case 2:
        print('Второй словарь является подмножеством первого.')
    case 3:
        print('Cловари с одинаковыми множествами.')
    case _:
        print('Ни один словарь не является подмножеством другого.')
#
set1 = {dict1.popitem() for item in range(len(dict1) - 1, -1, -1)}
set2 = {dict2.popitem() for item in range(len(dict2) - 1, -1, -1)}

if set1 < set2:
    print('Первый словарь является подмножеством второго.')
elif set1 > set2:
    print('Второй словарь является подмножеством первого.')
elif set1 == set2:
    print('Cловари с одинаковыми множествами.')
else:
    print('Ни один словарь не является подмножеством другого.')
#
'''
Напишите программу, которая заменяет числовые значения в словаре на их строковое представление (например, 1 → "один").
Используйте заранее подготовленный словарь чисел.
Данные:
* Словарь сопоставлений
number_to_word = {1: "один", 2: "два", 3: "три"}
Исходные данные
data = {"x": 1, "y": 2, "z": 3, "a": 4, "b": 1}
Пример вывода:
{'x': 'один', 'y': 'два', 'z': 'три', "b": "один"}
'''
number_to_word = {1: "один", 2: "два", 3: "три"}
data = {"x": 1, "y": 2, "z": 3, "a": 4, "b": 1}
print()
print('Словарь сопоставлений:\n', number_to_word)
print('Исходные данные:\n', data)
data_replace = dict()
for key in data:
    value = data[key]
    if value in number_to_word:
        data_replace[key] = number_to_word[value]

print('Новый словарь:\n', data_replace)