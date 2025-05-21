'''
1. Логические операции.
   Напишите программу, которая получит два логических значения от пользователя и
   выведет результат логических операций and, or, not для этих значений,
   а также сравнение на равенство и неравенство. Для операции not используйте первое число.
   Продумайте в каком виде получать ввод от пользователя для логического значения.
'''
val1 = bool(input('Enter logical First Value (eny symbol - TRUE, empty - FALSE) --> '))
val2 = bool(input('Enter logical Second Value (eny symbol - TRUE, empty - FALSE) --> '))

print('"First Value": ', val1, '\n"Second Value": ', val2)
print('"First Value" AND "Second Value": ', val1 and val2)
print('"First Value" OR "Second Value": ', val1 or val2)
print('not "First Value": ', not val1)
print('"First Value" EQUAL "Second Value": ', val1 == val2)
print('"First Value" NOT EQUAL "Second Value": ', val1 != val2)

'''
2. Проверка условий
   Напишите программу, которая принимает на вход логические значения двух переменных (свет включён и окно открыто) 
   и проверяет: Оба ли условия выполнены; Хотя бы одно из условий выполнено.
'''
SKIP = 8
light_on = bool(int(input('Введите условия: (1 - TRUE, 0 - FALSE) \n' + ' '*SKIP + 'Свет включён? --> ')))
door_open = bool(int(input(' '*SKIP + 'Окно открыто? --> ')))
print('Свет включён? ', light_on, '\nОкно открыто? ', door_open)
print('Оба условия выполнены? ', light_on and door_open, '\nХотя бы одно условие выполнено?', light_on or door_open)

'''
3. Стоимость мобильного тарифа
   Напишите программу для расчёта стоимости использования мобильного тарифа:
   Базовая стоимость: 30 евро. Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
   Программа должна запросить у пользователя количество использованных мегабайтов 
   и вывести сколько всего он заплатил (базовый и переплата).
'''
VOLUME_LIMIT = 500
COST_BASE = 30
PRICE_OVER = 0.2
text_input = ('Ваш базовый тариф: ' + str(COST_BASE) + ' евро (лимит: ' + str(VOLUME_LIMIT) + 'МБ).\n'
        + ' '*SKIP + 'Введите использованные мегабайты --> ')

volume_used = int(input(text_input))
# сначала сделал так:
# мы ещё не проходили условные операторы, поэтому будем считать, что пользователь вводит число больше лимита.
cost_full = COST_BASE + (volume_used - VOLUME_LIMIT) * PRICE_OVER
# но это конечно же элегантное решение!
cost_over = (volume_used - VOLUME_LIMIT) * PRICE_OVER
cost_full = COST_BASE + (volume_used >= VOLUME_LIMIT) * cost_over

print('Общая стоимость к оплате: ' + str(cost_full))
