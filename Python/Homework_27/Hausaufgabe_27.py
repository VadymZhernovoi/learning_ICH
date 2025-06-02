'''
1.  Фильтрация по ключевому слову
    Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
    Имя нового файла формируется как <keyword>_<original_filename>.
    Если файл не существует, программа должна вывести ошибку.
    Если совпадения не найдены, новый файл не создаётся.
    Используйте файл system_log.txt.
    Пример ввода:
    Введите имя файла для поиска: system_log.txt
    Введите ключевое слово: error
    Пример вывода:
    Строки, содержащие 'error', сохранены в error_system_log.txt.
'''
import os
def write_file(lines: list, file, mode: int = 0):
    w_a = [("w","a"), ("сохранены","добавлены")]
    with open(file, w_a[0][mode], encoding="utf-8") as file_write:
        file_write.writelines(lines)
    print(f"Строки, содержащие '{word}' {w_a[1][mode]} в {file}")

try:
    file1 = input("Введите имя файла для поиска --> ")
    if not os.path.exists(file1):
       raise FileExistsError(f"файл {file1} в текущей папке {os.getcwd()} не найден!")
    word = input("Введите ключевое слово --> ").lower()
    file2 = f"{word}_{file1}" # = word + "_" + file1
    lines_found = list()
    with open(file1, "r", encoding="utf-8") as file_in:
        for line in file_in:
            if word in line.lower():
                lines_found.append(line)

    if not lines_found:
        print(f"Ни одной строки, содержащей '{word}', в {file1} не найдены")
    else:
        if os.path.exists(file2):
            mode = int(input(f"Файл {file2} уже существует в текущей папке {os.getcwd()}.\n"
                         f"Укажите режим записи (0 - записать файл заново, 1 - дописать в конец файла) --> "))
            if 0 < mode > 1:
                raise ValueError("неверно указан режим записи в файл (0 - записать файл заново, 1 - дописать в конец файла)!")
            write_file(lines_found, file2, mode)
        else:
            write_file(lines_found, file2)

except FileExistsError as e:
    print(f"Ошибка: {e}")
except ValueError as e:
    print(f"Ошибка: {e}")

'''
2.  Поиск и удаление дубликатов
    Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
    Имя нового файла формируется как unique_<original_filename>.
    Если файл не существует, программа должна вывести ошибку.
    Исходный порядок строк должен сохраниться.
    Если в файле нет дубликатов, создаётся точная копия файла.
    Используйте файл movies_to_watch.txt.
    Пример ввода:
    Введите имя файла: movies_to_watch.txt
    Пример вывода:
    Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt
'''

try:
    file1 = input("Введите имя файла --> ")
    if not os.path.exists(file1):
        raise FileExistsError(f"файл {file1} в текущей папке {os.getcwd()} не найден!")
    file2 = f"unique_{file1}"
    with (open(file1, "r", encoding="utf-8") as file_in, open(file2, "w", encoding="utf-8") as file_out):
        lines_origin = set()
        lines_new = list()
        for line in file_in:
            if not line in lines_origin:
                lines_new.append(line)
                lines_origin.add(line)
        if lines_new:
            file_out.writelines(list(lines_new))
            print(f"Дубликаты удалены. Уникальные строки сохранены в {file2}.")
    # или так, но это как-то не очень(
    lines_new = dict()
    with (open(file1, "r", encoding="utf-8") as file_in, open(file2, "a", encoding="utf-8") as file_out):
        for line in file_in:
            lines_new[line] = ''
        if lines_new:
            file_out.writelines("\nВариант через словарь:\n\n")
            file_out.writelines(list(lines_new))
            print(f"Дубликаты удалены. Уникальные строки сохранены в {file2}.")

except FileExistsError as e:
    print(f"Ошибка: {e}")
