'''
1.  Прогрессия увеличения
    Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
    Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
numbers = (3, 7, 2, 8, 5, 10, 1)
'''
numbers = (3, 7, 2, 8, 5, 10, 1)
asc_tuple = ()

for ind, number in enumerate(numbers[:-1], start = 1):
    if number > numbers[ind] or ind == 1:
        asc_tuple += (number, )
    # print(number, numbers[ind], asc_tuple)

print('Кортеж по возрастанию:', asc_tuple)

'''
2.  Повторяющиеся элементы
    Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. 
    Вывести сами элементы и их индексы.
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
'''
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9, 5, 9, 9, 5)
import time

# сначала сделал так
print('\nВариант #1')
start = time.time()

item_up = ()
for item in numbers:
    if item not in item_up and numbers.count(item) > 1:
        print(f'Индексы элемента {item}:', end=' ')
        for ind, number in enumerate(numbers):
            if number == item:
                print(ind, end=' ')
        item_up += (item, )
        print()

stop = time.time()
print('Время:', stop - start)

# но другие варианты, я думаю, оптимальней по скорости
print('\nВариант #2')
start = time.time()

enumer_numbers = list(enumerate(numbers))
max = len(numbers)
item_up = ()

for item in numbers:
    if item not in item_up and numbers.count(item) > 1:
        print(f'Индексы элемента {item}:', end=' ')
        for ind in range(max):
            if enumer_numbers[ind][1] == item:
                print(ind, end=' ')
        item_up += (item, )
        print()

stop = time.time()
print('Время:', stop - start)

# или так должно быть ещё быстрее и памяти меньше
print('\nВариант #3')
start = time.time()

item_up = ()

for item in numbers:
    if item not in item_up and numbers.count(item) > 1:
        print(f'Индексы элемента {item}:', end=' ')
        i = 0
        for j in range(numbers.count(item)):
            ind = numbers.index(item, i)
            print(ind, end=' ')
            i = ind + 1
        item_up += (item, )
        print()

stop = time.time()
print('Время:', stop - start)