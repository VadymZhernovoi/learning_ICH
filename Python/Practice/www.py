'''
Напишите программу, которая проверяет, содержатся ли в двух заданных словарях одинаковые ключи.
Вывести одинаковые ключи или "-", если таковых нет.
Данные:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "d": 7, "a": 8}
Пример вывода:
Общие ключи: ['a', 'b']
'''
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "d": 7, "a": 8}
result = []
for key in dict1.keys():
    if key in dict2.keys():
        result.append(key)
print('Общие ключи:', result)

'''
Строки с длиной
Напишите программу, которая преобразует список строк в словарь, где ключи — сами строки, а значения —
их длины.
Данные:
words = ["apple", "banana", "cherry", "date"]
Пример вывода:
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
'''
words = ["apple", "banana", "cherry", "date"]
dict_words = dict()
for word in words:
    dict_words.setdefault(word, len(word))

print(dict_words)

'''
Напишите программу, которая удаляет из словаря все пары "ключ-значение", где значение пустое (например,
None, пустая строка или пустой список).
Данные:
data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
Пример вывода:
{'b': 2, 'e': [1, 2]}
'''
# data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
# for key, value in data.items():
#     if data.get(key) in (None ):
#         print(data.get(key))

'''
Вам дан словарь, где ключи — номера страниц книги, а значения — содержимое страниц. Некоторые
страницы отсутствуют (значения None). Напишите программу, которая на пропущенных страницах заменит
значение на "Страница потеряна".
Данные:
book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
Пример вывода:
Введите размер координатной сетки: 3
Координаты: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
'''
book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
for key, value in book.items():
    if book.get(key) == None:
        book[key] = "Страница потеряна"
print(book)

'''
База оценок студентов
У вас есть словарь с именами студентов и списками их оценок. Напишите программу, которая вычисляет
средний балл для каждого студента. Далее нужно сохранить средний балл в значениях для каждого студента,
как показано на примере.
Данные:
grades = {
 "anna": [5, 4, 3, 5],
 "bennet": [3, 2, 4],
 "john": [5, 5, 5]
}
Пример вывода:
{'anna': {'оценки': [5, 4, 3, 5], 'средний балл': 4.25}, 'bennet': {'оценки': [3, 2, 4], 'средний балл': 3.0},
'john': {'оценки': [5, 5, 5], 'средний балл': 5.0}}
'''
grades = {
 "anna": [5, 4, 3, 5],
 "bennet": [3, 2, 4],
 "john": [5, 5, 5]
}
result = dict()
for key, value in grades.items():
    result.setdefault(key, {'оценки':list(value), 'средний балл': sum(value)/len(value)})
print(result)

'''
Рецепты по ингредиентам
Создайте словарь, в котором для каждого набора ингредиентов будут храниться все названия рецептов.
Учитывайте что ингредиенты могут быть перечислены в произвольном порядке и некоторые рецепты могут
иметь одинаковые ингредиенты.
Выведите возможные рецепты для каждого набора продуктов.
В конце пользователь вводит список имеющихся у него ингредиентов через пробел, и программа должна
вывести названия всех доступных рецептов. Если рецептов нет, нужно вывести сообщение "Нет рецептов".
Данные:
recipes = {
 ("flour", "egg", "milk"): "Pancakes",
 ("egg", "milk", "butter"): "Omelette",
 ("flour", "sugar", "butter"): "Cookies",
 ("flour", "egg", "butter", "sugar"): "Cake",
 ("milk", "flour", "egg"): "Waffles",
 ("butter", "milk", "egg"): "Scrambled Eggs",
 ("flour", "milk", "sugar", "butter"): "Sweet Bread"
}
Пример вывода:
milk egg butter flour
'''
# recipes = {
#  ("flour", "egg", "milk"): "Pancakes",
#  ("egg", "milk", "butter"): "Omelette",
#  ("flour", "sugar", "butter"): "Cookies",
#  ("flour", "egg", "butter", "sugar"): "Cake",
#  ("milk", "flour", "egg"): "Waffles",
#  ("butter", "milk", "egg"): "Scrambled Eggs",
#  ("flour", "milk", "sugar", "butter"): "Sweet Bread"
# }
# for key, value in recipes.items():
#     print(value, ':', key)
# not_is = True
# engrad = input('Enter products: ').lower().split()
# for key, value in recipes.items():
#     if set(engrad) <= set(key):
#         print(engrad, ':', value)
#         not_is = False
# if not_is:
#     print("Нет рецептов")

'''
Одинаковые предметы
Есть список студентов и наборы предметов, которые они изучают.
Необходимо сгруппировать студентов по идентичным наборам предметов, используя frozenset как ключ, и
вывести группы.
Данные:
students = {
 "Alice": ["Math", "Physics"],
 "Bob": ["Math", "Physics"],
 "Charlie": ["Chemistry", "Biology"],
 "David": ["Math", "Physics"],
 "Eve": ["Chemistry", "Biology"]
}
Пример вывода:
Группа с предметами: Physics, Math: ['Alice', 'Bob', 'David']
Группа с предметами: Biology, Chemistry: ['Charlie', 'Eve']
'''
students = {
 "Alice": ["Math", "Physics"],
 "Bob": ["Math", "Physics"],
 "Charlie": ["Chemistry", "Biology"],
 "David": ["Math", "Physics"],
 "Eve": ["Chemistry", "Biology"]
}
result = dict()
for key, value in students.items():
    item = list(result.setdefault(frozenset(value), {}))
    item.append(key)
    result[frozenset(value)] = item
for key, value in result.items():
    group = list(key)
    print('Группа с предметами:', end=' ')
    print(*group, sep =', ', end=' ')
    print(':', list(value))