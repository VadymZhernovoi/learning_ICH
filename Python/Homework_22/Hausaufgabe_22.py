'''
1.  Выбор заказов
    У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
    Напишите функцию, которая:
    Отбирает заказы дороже 500.
    Создаёт список названий отобранных продуктов в алфавитном порядке.
    Возвращает итоговый список названий.
Данные:
orders = [
{"product": "Laptop", "price": 1200},
{"product": "Mouse", "price": 50},
{"product": "Keyboard", "price": 100},
{"product": "Monitor", "price": 300},
{"product": "Chair", "price": 800},
{"product": "Desk", "price": 400}
]
Пример вывода:
['Chair', 'Laptop']
'''
from collections import OrderedDict

orders = [
{"product": "Laptop", "price": 1200},
{"product": "Mouse", "price": 50},
{"product": "Keyboard", "price": 100},
{"product": "Monitor", "price": 300},
{"product": "Chair", "price": 800},
{"product": "Desk", "price": 400}
]

def filter_orders(orders, price_over=500):
    ''' Отбирает заказы дороже "price_over" (default 500). Создаёт список названий отобранных продуктов в алфавитном порядке.
        \nВозвращает итоговый список названий. '''
    products = filter(lambda product: product["price"] > price_over, orders)

    return sorted(map(lambda product: product["product"], products))

print(filter_orders(orders))
print(filter_orders(orders, price_over=100))

'''
2.  Статистика продаж
    Дан список продаж в виде кортежей (товар, количество, цена).
    Напишите программу, которая:
    Вычисляет общую выручку для каждого товара.
    Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.

Данные:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
'''
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Mouse", 580, 15),
    ("Chair", 20, 800),
    ("Keyboard", 40, 450)
]

def get_value(item): # для второго варианта сортировки
    return item[1]

def get_sum_product(products, sort=True, revers=True):
    ''' Вычисляет общую выручку для каждого товара.
        Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки. '''
    sales = {}
    for product, quant, price in products:
        sales[product] = sales.get(product, 0) + (quant * price) # для случая, когда будет несколько строк с одним и тем-же товаром
    if not sort:
        return sales
    result = sorted(sales.items(), key=lambda i: i[1], reverse=revers)
    # или второй вариант
    result = sorted(sales.items(), key=get_value, reverse=revers)
    return dict(result)

print()
print(get_sum_product(sales))
print(get_sum_product(sales,sort=False))
print(get_sum_product(sales,revers=False))

