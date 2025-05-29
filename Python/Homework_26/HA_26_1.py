'''
1.  Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
        Отдельно список папок
        Отдельно список файлов
    Пример запуска
    python script.py /home/user/documents
    Пример вывода
    Содержимое директории '/home/user/documents':
    Папки:
    - folder1
    - folder2
    Файлы:
    - file1.txt
    - file2.txt
    - notes.docx
'''
import os
import sys

if len(sys.argv) == 1:
    print("Ошибка: отсутствует аргумент <путь к директории>.")
    sys.exit(1)
path = sys.argv[1]
if not os.path.exists(path):
    print("Ошибка: папка", path, "не существует!")
    sys.exit(1)

os.chdir(path)

files = list()
dirs = list()
for item in os.listdir(path):
    if os.path.isfile(item):
        files.append(item)
    else:
        dirs.append(item)

print(f"Содержимое директории '{path}':")
print("Папки:")
for item in dirs:
    print("-", item)
print("Файлы:")
for item in files:
    print("-", item)