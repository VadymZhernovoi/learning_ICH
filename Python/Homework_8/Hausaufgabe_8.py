'''
1. Напишите программу, которая принимает от пользователя один символ и выводит его код в таблице Unicode
и его принадлежность к диапазону ASCII (True/False).
'''
from operator import concat

symb = input('Введите один символ --> ')

print('Код Unicode:', ord(symb))
print('ASCII символ:', ord(symb) <= 127)

'''
2. Подстрока с заполнением
Напишите программу, которая принимает строку и индексы начала и конца. 
Программа должна вывести подстроку на указанных позициях. 
Также если конечный индекс выходит за пределы строки, программа заполняет недостающие символы символами _.
'''
string = input('Введите строку --> ')
i_from = int(input('Введите начальный индекс --> '))
i_to = int(input('Введите конечный индекс --> '))
# string = 'Программирование'
# i_from = 3
# i_to = 5
# если включая конечный индекс
str_new = string[i_from:i_to+1]
if i_to > len(string[i_from:i_to]) :
    str_new +=  '_' * (i_to - len(string) + 1)

print('Подстрока (включая конечный индекс):', str_new)

# если не включая конечный индекс
str_new = string[i_from:i_to]
if i_to > len(string[i_from:i_to]) :
    str_new +=  '_' * (i_to - len(string))

print('Подстрока (не включая конечный индекс):', str_new)

'''
3. Напишите программу, которая принимает строку и символ, а затем подсчитывает, сколько раз символ встречается в строке.
'''
string = input('Введите строку --> ')
symb = input('Введите символ --> ')
# string = 'Hello, world!'
# symb = 'o'
cnt = 0
i = 0
while i < len(string):
    if string[i] == symb:
        cnt += 1
    i += 1

if cnt > 1:
    print('Символ "' + symb + '" встречается ' + str(cnt) + ' раз(а).')
else:
    print('Строка "' + string + '" не содержит символ "' + symb + '".')

'''
4. Инвертирование строки без цифр
Напишите программу, которая принимает строку и выводит её в обратном порядке, пропуская все цифры.
'''
string = input('Введите строку --> ')
# string = 'n92uFs6Inoh67ty0P'
string_inv = ''
i = 0
while i < len(string):
    if not 48 <= ord(string[i]) <= 57:
        string_inv += string[i]
    i += 1
string_inv = string_inv[::-1]

print('Результат: ', string_inv)


