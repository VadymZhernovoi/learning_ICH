"""
1.  Создание базы
    Напишите программу, которая:
        создаёт базу данных notes_app_<your_group>_<your_full_name>
        выбирает эту базу через USE notes_app
        выводит сообщение о результате
Пример вывода:
Database 'notes_app' created or already exists.
"""
import pymysql
from pymysql.cursors import DictCursor

config = {
    "host": "ich-edit.edu.itcareerhub.de",
    "user": "ich1",
    "password": "ich1_password_ilovedbs",
    "cursorclass": DictCursor}

connection = pymysql.connect(**config)

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        try:
            db_name = "notes_app_210225_Zhernovoi"
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")

            cursor.execute("SHOW TABLES") # проверяем на selected 
        except pymysql.err.OperationalError:
            print(f"Database '{db_name}' not selected or not created.")
            exit()

        print(f"Database '{db_name}' created or already exists.")

        # 2.  Добавление заметок
        #     Продолжите предыдущую программу:
        #         создайте таблицу notes с полями: id, title, content
        #         вставьте одну заметку в таблицу
        #         выполните commit() после вставки
        #         выведите все заметки используя DictCursor
        # Пример вывода:
        # Note added: Shopping list

        cursor.execute("""CREATE TABLE IF NOT EXISTS notes 
                            (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100), content text)""")

        import datetime
        title = f"Don't forget {datetime.datetime.now() + datetime.timedelta(days=7):%d.%m.%Y}!"
        with open("german_numbers.txt", "r", encoding="utf-8") as f: # so as not to forget
            content = f.read()

        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))

        connection.commit()

        cursor.execute("SELECT * FROM notes")
        result = cursor.fetchall()  # будем выводить все заметки, хотя по заданию добавили одну )
        print("Note added:")
        for row in result:
            print(f"{row["title"]}\n{row["content"]}\n")
