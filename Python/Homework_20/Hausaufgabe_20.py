'''
1.  Простое число
    Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя)
    и возвращает булевый результат.
    Данные: n = 17
    Пример вывода:
    Число 17 является простым
'''
def is_prime(number):
    ''' Function checks whether "number" is prime'''
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

n = int(input('Введите целое число --> '))
print('Число ' , n, '' if is_prime(n) else ' не', ' является простым', sep='')

# list = [n for n in range(100) if is_prime(n)]
# print(list)
#
'''
2.  Фильтрация чисел по чётности
    Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, 
    возвращая только те, которые соответствуют фильтру.
    Пример вызова:
    print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
    print(filter_numbers("odd", 10, 15, 20, 25))
    print(filter_numbers("prime", 2, 3, 5, 7))
    Пример вывода:
    [2, 4, 6]
    [15, 25]
    Некорректный фильтр
'''
def filter_numbers(filter_type, *args):
    '''function accepts filter_type (“even” or “odd”) and an arbitrary number of numbers,
    returning only those that match the filter.'''
    print(f'В функцию "filter_numbers" передан фильтр "{filter_type}" и следующие числа: {list(args)}') # zum Spaß
    filter_type = filter_type.lower()

    if filter_type != "even" and filter_type != "odd":
        return 'Некорректный фильтр'
    if filter_type == "even":
        return [n for n in args if n % 2 == 0]
    else:
        return [n for n in args if n % 2 != 0]
print()
print('Результат:', filter_numbers("Even", 1, 2, 3, 4, 5, 6))
print('Результат:', filter_numbers("ODD", 10, 15, 20, 25))
print('Результат:', filter_numbers("prime", 2, 3, 5, 7))

'''
3.  Объединение словарей
    Напишите функцию, которая принимает любое количество словарей и объединяет их в один. 
    Если ключи повторяются, используется значение из последнего словаря.
    Данные:
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    dict3 = {"d": 5}
    Пример вызова:
    print(merge_dicts(dict1, dict2, dict3))
    Пример вывода:
    {'a': 1, 'b': 3, 'c': 4, 'd': 5}
'''
def merge_dicts(*args):
    '''Function accepts any number of dictionaries and combines them into one.
    If the keys are repeated, the value from the last dictionary is used.'''
    new_dict = dict()
    print('В функцию "merge_dicts" переданы следующие словари:') # zum Spaß
    i = 0
    for item in args:
        i += 1
        print(f'dict{i} = {item}') # zum Spaß
        for key, value in item.items():
            new_dict[key] = value
    return new_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print()
print('Итоговый словарь:\n', merge_dicts(dict1, dict2, dict3))