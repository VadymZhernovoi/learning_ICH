'''
1.  Число в конце
    Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка,
    в которых цифры находятся только в конце.

Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
'''
strings = ["*a-a:a b.b,b+", "apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

print('Исходный список:', strings)
strings_res = []

for string in strings:
    i = 0
    while i < len(string):
        if string[i].isdigit():
            break
        i += 1
    else:
        continue
    #print(string, i)
    if string[i:].isdigit():
        strings_res.append(string)

print('Строки с цифрами только в конце: ', strings_res)

'''
2.  Удаление кратных
    Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
'''
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
print()
print('Список исходных значений: ', numbers)
num = int(input('Введите число для удаления кратных ему элементов --> '))

numbers_res = list()
for n in numbers:
    if n % num != 0:
        numbers_res.append(n)

print('Список без кратных значений:', numbers_res)

'''
3.  Порядок четных
    Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, 
    где: нечетные числа занимают те же позиции, чётные числа отсортированы между собой обратном порядке.
'''
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
print()
print('Список исходных значений: ', numbers)

numbers_res = []
numbers_sort = []
for n in numbers:
    if n % 2 == 0:
        numbers_sort.append(n)
numbers_sort.sort(reverse=True)
#print(numbers_sort)
i = 0
for n in numbers:
    if n % 2 != 0:
        numbers_res.append(n)
    else:
        numbers_res.append(numbers_sort[i])
        i += 1

print('Список после сортировки:', numbers_res)
