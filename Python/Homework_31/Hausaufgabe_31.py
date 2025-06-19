'''
1.  Извлечение дат
    Реализуйте программу, которая должна:
    Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022
'''
import re
pattern = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}\.\d{2}\.\d{4}"
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
print("итератор finditer:")
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())

print("список findall:")
matches = re.findall(pattern, text)
for match in matches:
    print(match)

'''
2.  Разделение списка тегов
    Реализуйте программу, которая должна:
    Прочитать строку с тегами, введёнными пользователем.
    Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).
    Удалить лишние пробелы и пустые значения.
Данные:
tag_input = "python, data-science / machine-learning; AI neural-networks"
Пример вывода:
['python', 'data-science', , 'machine-learning', 'AI', 'neural-networks']
'''
tag_input = "python  ,, data-science   // , ; / machine-learning; AI neural-networks"
print()
pattern = r"[^,;/\s]+"
print("findall:")
matches = re.findall(pattern, tag_input)
print(matches)
# Удалить лишние пробелы и пустые значения.
matches = [tag.strip() for tag in re.findall(pattern, tag_input) if tag] # хотя это лишнее - '\s' и '+' и так не дают лишних пробелов и пустых значений
print(matches)

print("split:")
matches = re.split(r"[,;/\s]+", tag_input)
print(matches)