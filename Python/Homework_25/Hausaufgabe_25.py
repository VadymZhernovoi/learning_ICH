'''
1.  Деление без ошибок
    Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
    Пример вывода:
    Введите делимое: 345
    Введите делитель: 5a
    Ошибка: Введено некорректное число.
'''
def numb_division(a: float, b: float) -> float:
    '''
    Деление двух чисел
    :param a: делимое
    :param b: делитель
    :return: результат деления
    '''
    try:
        result = float(a) / float(b)
    except ValueError:
        print("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        print("Ошибка: Делитель не может быть равен 0.")
    else:
        return result

a = input("Введите делимое --> ")
b = input("Введите делитель --> ")
c = numb_division(a, b)
if c != None:
    print(f"Результат: {a} / {b} = {c}")

'''
2.  Логирование ошибок
    Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
    Пример вывода:
    2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.
'''
import logging
logging.basicConfig(filename="errors.log",
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
                    level=logging.INFO)
def numb_division_log(a: float, b: float) -> float:
    '''
    Деление двух чисел
    :param a: делимое
    :param b: делитель
    :return: результат деления
    '''
    try:
        result = float(a) / float(b)
    except ValueError:
        logging.error("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        logging.error("Ошибка: Делитель не может быть равен 0.")
    else:
        return result

print()
a = input("Введите делимое --> ")
b = input("Введите делитель --> ")
c = numb_division_log(a, b)
print(f"Результат: {a} / {b} = {c}" if c != None else "Были введены некорректные параметры функции")