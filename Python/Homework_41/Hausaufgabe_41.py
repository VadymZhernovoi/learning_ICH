"""
1.  Список всех стран.
    Используя базу данных world, выведи названия всех стран из таблицы country.
    Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe
"""

import pymysql

BATCH_DEFAULT = 25


def get_batch_cnt(rec_all, batch_size=100):
    return rec_all // batch_size + 1


def get_batch(cursor, result, batch_size=100):
    for row in cursor.fetchmany(batch_size):
        result.append((row[0], row[1]))


config = {"host": "ich-db.edu.itcareerhub.de",
          "user": "ich1",
          "password": "password",
          "database": "world", }

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        countries = list()
        rec_all = cursor.execute(f"SELECT name, code FROM country")
        batch_all = get_batch_cnt(rec_all, BATCH_DEFAULT)
        for _ in range(batch_all):
            get_batch(cursor, countries, BATCH_DEFAULT)

        for i, item in enumerate(countries, 1):
            print(f"{i}. {item[0]} ")

        # 2.  Города выбранной страны.
        #     Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка.
        #     Далее выведите все города этой страны и их численность населения, также с нумерацией.
        # Пример вывода:
        # Введите страну: Germany
        # 1. Berlin - 3386667
        # 2. Hamburg - 1704735
        # 3. Munich [München] - 1194560
        # ...
        string = input("Введите страну (или номер страны) из списка --> ")
        country_sel = list()
        if string.isdigit():
            num = int(string)
            if 1 <= num <= len(countries):
                enumerate(countries, 1)
                country_sel = countries[num - 1]
            else:
                print(f"Ошибка! Страна под номером {string} в списке стран не найдена.")
        else:
            try:
                country_sel = tuple(filter(lambda x: x[0] == string, countries))[0]
            except IndexError:
                print(f"Ошибка! Страна {string} в списке стран не найдена.")
                pass

        if country_sel:
            cities = list()
            rec_all = cursor.execute("SELECT name, population FROM city WHERE CountryCode = %s", (country_sel[1],))
            batch_all = get_batch_cnt(rec_all, BATCH_DEFAULT)
            for _ in range(batch_all):
                get_batch(cursor, cities, BATCH_DEFAULT)

            for i, item in enumerate(cities, 1):
                print(f"{i}. {item[0]} - {item[1]}")

