'''
1. Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
'''
text = "My number is 123-456-789"

print('Строка:', text)

for i in range(0,10):
    text = text.replace(str(i), '*')

print('Результат:', text)

'''
2. Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. 
Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. 
Выводите повторяющиеся символы только один раз.
text = "Programming in python"
'''
text = "Programming in python"

text_lower = text.lower()
chr_up = ''
for chr in text_lower:
    if text_lower.count(chr) > 1 and chr not in chr_up:
        print("Символ '" + chr + "' встречается " + str(text_lower.count(chr)) + " раз(а)")
        chr_up += chr

'''
3. Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
'''
text = "I have 5 apples and 10 oranges, price is 2.01 each. Card number is ....3672."
print('Было: ', text)

from decimal import Decimal # приходиться использовать для корректности операций для чисел с запятой:(

text_arr = text.split()
for i in range(0,len(text_arr)):
    if text_arr[i].isdecimal():
        text_arr[i] = str(int(text_arr[i]) * 10)
    elif text_arr[i].count('.') == 1: # т.к. обработку ошибок мы ещё не проходили, то float() использовать не получится.
                                      # поэтому получаем доступными на сегодня способами вещественное число (float)
        # print(float(text_arr[i]) * 10)
        if text_arr[i].split(sep='.')[0].isdecimal() and text_arr[i].split(sep='.')[1].isdecimal():
            text_arr[i] = str(Decimal(text_arr[i]) * 10) # приходиться использовать для корректности операций для чисел с запятой:(
text = ' '.join(text_arr)

print('Стало: ', text)