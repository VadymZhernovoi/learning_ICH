'''
1. Сумма цифр числа
Напишите программу, которая вычисляет сумму цифр введённого числа.
'''
num = int(input('Введите число --> '))
# num = 123456
sum = 0
while num > 0:
    sum += num % 10
    num //= 10

print('Сумма цифр: ', sum)

'''
2. Палиндром
Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно палиндромом. 
Число является палиндромом, если оно читается одинаково слева направо и справа налево.
'''
print('')
num = int(input('Введите число --> '))
# num = 12321
num_inv = 0
num_tmp = num

while num_tmp > 0:
    num_inv = num_inv * 10 + num_tmp % 10
    num_tmp //= 10

print('Число ', num, '' if num_inv == num else ' не', ' является палиндромом. ', sep='')

# ну или
symb_inv = ''
num_tmp = num

while num_tmp > 0:
    symb_inv = symb_inv + str(num_tmp % 10)
    num_tmp //= 10
not_poli = ' не' if int(symb_inv) != num else ''

print('Число ' + str(num) + not_poli + ' является палиндромом.')

'''
3. Проверь интуицию
Напишите программу, которая генерирует случайное число от 1 до 100 включительно и дает пользователю 10 попыток, 
чтобы угадать это число. Программа должна подсказывать, больше или меньше загаданное число. 
После завершения игры программа оценивает, насколько хорошая интуиция у игрока.
'''
from random import randint
CNT_I = 10 # 5
RAN_START = 1
RAN_STOP = 100 #10
print('')

while True:
    num_win = randint(RAN_START, RAN_STOP)
    i = 1
    # print(num_win)

    print('Угадайте число от ' + str(RAN_START) + ' до ' + str(RAN_STOP) + '. У вас ' + str(CNT_I) + ' попыток.\n')
    while i <= CNT_I:
        txt_inp = 'Попытка номер ' + str(i) + ' --> ' if i == 1 else 'Попытка номер: ' + str(i) + ' --> '
        num = int(input(txt_inp))
        if num < RAN_START or num > RAN_STOP:
            print('Внимание, ошибка! Введите число от ', RAN_START,  ' до ', RAN_STOP)
            continue
        if num == num_win:
            break
        i += 1
        print('Загаданное число меньше вашего.\n' if num_win < num else 'Загаданное число больше вашего.\n')
    else:
        print('К сожалению Вы не угадали число: ' + str(num_win) + '. Не отчаивайтесь!')

        flag = int(input('\nПопробуете еще раз (1 - Да, 0 - Закончить)? --> '))
        if flag == 0:
            print('Заходите ещё!')
            break

    match i:
        case 1:
            txt_att = ' попытку.'
        case 2|3|4:
            txt_att = ' попытки.'
        case _:
            txt_att = ' попыток.'
    stp = (CNT_I - 1) // 3
    txt_first = ('Поздравляем! Вы угадали число: ' + str(num_win) + '\nВы угадали число за ' + str(i) + txt_att) + ' '
    if  i == 1:
        txt_first = txt_first + 'Отличный результат!\nОтличная интуиция! Вы угадали с первой попытки!'
    elif i == CNT_I:
        txt_first = 'Вы вскочили в последний вагон! Вы угадали число: ' + str(num_win) + ' за крайнюю попытку'
    elif i <= stp:
        txt_first = txt_first + 'Отличный результат!'
    elif i <= stp * 2:
        txt_first = txt_first + 'Хороший результат!'
    else:
        txt_first = txt_first + 'Это тоже результат!'

    print(txt_first)

    flag = int(input('\nХотите сыграть еще раз (1 - Да, 0 - Закончить)? --> '))
    if flag == 0:
        print('Заходите ещё!')
        break
