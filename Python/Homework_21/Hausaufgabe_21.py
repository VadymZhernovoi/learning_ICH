'''
1.  Повторения букв
    Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
    Данные: text = "Programming is fun!"
    Пример вывода:
    {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
'''
text = "9 Programming is fun!"

from collections import Counter

def count_letter_v1(text):
    ''' Function accepts text and returns a dictionary with a count of the number of each letter, ignoring case '''
    # одной строкой
    return {chr: number for chr, number in Counter(text.lower()).items() if chr.isalpha()}
    # или так
    # result = dict()
    # for chr, number in Counter(text.lower()).items():
    #     if chr.isalpha():
    #         result[chr] = number
    # return result
# или
def count_letter_v2(text):
    ''' Function accepts text and returns a dictionary with a count of the number of each letter, ignoring case '''
    for chr in text.lower():
        if not chr.isalpha():
            text = text.replace(chr, '')
    return dict(Counter(text))

print(text)
print(count_letter_v1(text))
print(count_letter_v2(text))

'''
2.  Группировка студентов по классам
    Создайте структуру для группировки студентов по классам.
    Добавьте студентов в соответствующие группы.
    Данные: students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
    Пример вывода:
    {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
'''
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

from collections import defaultdict

def grouping_students(students_list):
    ''' Function groups students into classes '''
    groups = defaultdict(list)
    for clas, name in students_list:
        groups[clas].append(name)
    return dict(groups)

print()
print(students)
print(grouping_students(students))