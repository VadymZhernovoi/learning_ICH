'''
1.  Одно слово
    Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова,
    а также преобразует оставшиеся строки к нижнему регистру.

    Данные: text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
'''
text_list = ["Hello", "Python   Programming", "World", "Advanced Topics", "Simple", "12", "1 2"]
print("Исходный список:", text_list)

# сделаем без создания нового списка
for i in range(len(text_list)-1, -1, -1): # будем удалять с конца
    if len(text_list[i].split()) > 1:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()

print("Обработанный список:", text_list)

'''
2.  Обновление цен товаров
    Дан список товаров с ценами. Программа должна применить скидку к каждому товару 
    и добавить в список элемент с новой ценой. 
    В конце вывести таблицу с новой ценой.
    
    Данные: products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
'''
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

print()
discount = int(input('Введите скидку (в процентах) --> '))
#discount = 17

discount = discount / 100
for product in products:
    price_new = product[1] - product[1] * discount
    product.append(price_new)

# В конце вывести таблицу с новой ценой.
print(f'{"Товар":12} {"Старая цена":>11} {"Новая цена":>11}')
print('-'*12, '-'*11, '-'*11)
for product in products:
    print(f'{product[0]:12} {product[1]:10.2f}$ {product[2]:10.2f}$')

#print(products)

