import os
import sys
from dataclasses import replace

'''
2.  Поиск и удаление файлов с указанным расширением
    Напишите программу, которая:
    Принимает путь к директории и расширение файлов через аргумент командной строки.
    Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
    Спрашивает у пользователя, хочет ли он удалить найденные файлы.
    Если пользователь подтверждает, удаляет их.
    Пример запуска:
    python script.py /home/user/PycharmProjects/project1 .log
    Пример вывода
    Найдены файлы с расширением '.log':
    - logs/error.log
    - logs/system.log
    - logs/backup/old.log
    - logs/backup/debug.log
    Вы хотите удалить эти файлы? (y/n): y
    Удаление завершено.
'''
def get_files(files: list, delete: str='n'):
    for file in files:
        if delete.lower() == "y":
            if os.path.exists(file):
                os.remove(file)
                print(file.replace('./', ''), "- удалён")
        else:
            print("-", file.replace('./', ''))

if len(sys.argv) == 1:
    print("Ошибка: отсутсвуют аргументы <путь к директории> и <расширение файлов>")
    sys.exit(1)
elif len(sys.argv) == 2:
    print("Ошибка: отсутсвует аргумент <расширение файлов>")
    sys.exit(1)
path = sys.argv[1]
ext = sys.argv[2]

if not os.path.exists(path):
    print("Ошибка: папка", path, "не существует!")
    sys.exit(1)

os.chdir(path)

found = list()
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(ext):
            print(os.path.relpath(file))
            found.append(os.path.join(root, file))
if found:
    print(f"Найдены файлы с расширением '.{ext}' :")
    get_files(found)
    delete = input("Вы хотите удалить эти файлы? (y/n): ")
    print(delete)
    if delete.lower() == "y":
        get_files(found, delete)
        print("Удаление завершено.")
else:
    print(f"Файлы с расширением .{ext} не найдены в папке '{path}' и во всех вложенных папках.")