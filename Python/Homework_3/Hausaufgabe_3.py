# Задание 1.

# вариант, который подсказывает сам PyCharm:)

number = int(input("1-й вариант. Введите четырехзначное целое число --> "))

dig4 = number // 1000
dig3 = number // 100 % 10
dig2 = number // 10 % 10
dig1 = number % 10

print("Результат: ", dig4, "+", dig3, "+", dig2, "+", dig1, " = ", dig4 + dig3 + dig2 + dig1, sep="")

# вариант через простые операции +,-,*,/

number = int(input("2-й вариант. Введите четырехзначное целое число --> "))

dig4 = int(number / 1000)
number -= dig4 * 1000
dig3 = int(number / 100)
number -= dig3 * 100
dig2 = int(number / 10)
number -= dig2 * 10

print("Результат: ", dig4, "+", dig3, "+", dig2, "+", number, " = ", dig4 + dig3 + dig2 + number, sep="")

# Задание 2.

number1 = int(input("Введите первое целое число --> "))
number2 = int(input("Введите второе целое число --> "))

print("Результат: " + str(number1 * number2), number1, number2, sep='-')

number1 = float(input("Введите первое число с точкой --> "))
number2 = float(input("Введите второе число с точкой --> "))

print("Результат: " + str(number1 * number2), number1, number2, sep='-')

# Задание 3.

# учитывая то, что мы на сегодня прошли, мы можем написать только для положительных чисел (т.к. ещё не изучали IF и т.д.)

number1 = int(input("Введите первое целое положительное число --> "))
number2 = int(input("Введите второе целое положительное число --> "))

print("Остаток от деления: ", number1 - number2 * int(number1 / number2), " (проверка: ", number1 % number2, ")", sep='')
print("Целочисленное деление: ", int(number1 / number2), " (проверка: ", number1 // number2, ")", sep='')

