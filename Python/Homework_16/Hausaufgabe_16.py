'''
1.  Оценки текстом
    Напишите программу, которая преобразует список оценок по системе от 1 до 5 в текстовое представление.
    Нужно сохранить в списках числовой результат и текстовое представление.
    Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".

    Данные: grades = [5, 3, 4, 2, 1, 5, 3]

    Пример вывода:
    [[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'], [1, 'неудовлетворительно'], [5, 'отлично'], [3, 'хорошо']]
'''
grades = [5, 3, 4, 2, 1, 5, 3]

grades_new = [[grade, 'отлично'] if grade == 5 else ([grade,'неудовлетворительно'] if grade < 3 else [grade,'хорошо'])
              for grade in grades]
print(grades_new)
# or
for grade in grades:
    if grade < 3:
        grade = [grade,'неудовлетворительно']
    elif grade == 5:
        grade = [grade, 'отлично']
    else:
        grade = [grade,'хорошо']
print(grades_new)

'''
2.  Правильные скобки
    Напишите программу, которая принимает строку, содержащую любые виды скобок — круглые (), квадратные [] и фигурные {}.
    Необходимо проверить, правильно ли они расставлены. Скобки считаются правильно расставленными, если:
    Каждая открывающая скобка имеет соответствующую закрывающую.
    Скобки закрываются в правильном порядке.

    Пример данных: string = "({[}])"
    Пример вывода:
    Скобки: ({[}])
    Валидны: False
    Скобки: ([({}()){}])
    Валидны: True
'''
import time
#string = "({[}])"
string = "([({}()){}])"
bkt_open = '([{'
bkt_close = ')]}'
valid = True
print('Скобки:', string)

start = time.time()

if (len(string) % 2 != 0 or
        string.count(bkt_open[0]) != string.count(bkt_close[0]) or
        string.count(bkt_open[1]) != string.count(bkt_close[1]) or
        string.count(bkt_open[2]) != string.count(bkt_close[2]) or
        string[0] in (bkt_close[0] or bkt_close[1] or bkt_close[2]) or
        string[-1] in (bkt_open[0] or bkt_open[1] or bkt_open[2])):
    valid = False
else:
    bkt_str = []
    for char in string:
        if char in (bkt_open[0], bkt_open[1], bkt_open[2]):
            bkt_str.append(char)
            #print( char, '+++', bkt_str)
        else:
            ind = bkt_close.index(char)
            if bkt_open[ind] != bkt_str.pop():
                valid = False
                break
            #else:
            #    print(char, '---', bkt_str)
print('Валидны:', valid)

stop = time.time()
print('Время:', stop - start)

# или так короче, но не во всех случаях быстрее

start = time.time()

valid = True
bkt_str = []
for char in string:
    if char in (bkt_open[0], bkt_open[1], bkt_open[2]):
        bkt_str.append(char)
    elif len(bkt_str) == 0:
        valid = False
        break
    else:
        ind = bkt_close.index(char)
        if bkt_open[ind] != bkt_str.pop():
            valid = False
            break
if len(bkt_str) > 0:
    valid = False
print('Валидны:', valid)

stop = time.time()
print('Время:', stop - start)