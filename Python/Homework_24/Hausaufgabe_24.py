'''
1.  Сумма цифр числа
    Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
    Данные: num = 43197
    Пример вывода: 24
'''
def sum_all_n(num: int) -> int:
    '''
     Функция находит сумму всех цифр числа
    :param num: число
    :return: сумма всех цифр числа
    '''
    if num < 10:
        return num
    # n = num % 10
    return num % 10 + sum_all_n(num // 10)

def sum_all_s(num: int, start: int = 0, acc: int = 0) -> int:  # потренироваться
    if start == len(str(num)):
        return acc
    n = int(str(num)[start])

    return acc + sum_all_s(num, start + 1, n)

num = 43197
print("sum_all_n :", sum_all_n(num))
print("sum_all_s :", sum_all_s(num))

'''
2.  Сумма вложенных чисел
    Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
    Данные: nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
    Пример вывода: 28
'''
def sum_num_list(items: list) -> int:
    '''
    Функция суммирует все числа во вложенных списках.
    :param numbers: список вложенных числовых списков
    :return: сумма всех чисел списка
    '''
    if type(items) == list:
        acc = 0
        for item in items:
            acc += sum_num_list(item)
        return acc
    else:
        return items

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(sum_num_list(nested_numbers))