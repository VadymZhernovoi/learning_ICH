'''
1.  Анализ курсов студентов
    Реализовать программу, которая должна:
    Прочитать файл student_courses.json, содержащий:
        имя,
        дату рождения (birth_date) в формате дд.мм.гггг,
        дату поступления (enrollment_date) в том же формате,
        список курсов.
    Вычислить:
        Общее количество студентов.
        Средний возраст на момент поступления.
        Количество студентов на каждом курсе.
        Сохранить отчёт в JSON-файл student_courses_report.json.
    Данные:
    [
    {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
    {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
    {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
    ...
    ]
Пример вывода (student_courses_report.json):
{
    "total_students": 100,
    "average_enrollment_age": 27.9,
    "students_per_course": {
        "Art": 21,
        "Biology": 18,
        "Business": 28,
        "Chemistry": 16,
        "Economics": 23,
        "History": 9,
        "Linguistics": 23,
        "Math": 23,
        "Philosophy": 19,
        "Physics": 19
    }
}
'''
import json
from datetime import datetime
from collections import defaultdict
report_json = defaultdict()
curs_count = defaultdict(int)
file_source = "student_courses.json"
file_report = "student_courses_report.json"
try:
    with (open(file_source, "r") as file_in, open(file_report, "w") as file_out):
        source_json = json.load(file_in)
        report_json["total_students"] = len(source_json)
        age_all = 0
        for student in source_json:
            birth_d = datetime.strptime(student["birth_date"], "%d.%m.%Y")
            enrollment_d = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
            age_all += enrollment_d.year - birth_d.year - ((enrollment_d.month, enrollment_d.day) < (birth_d.month, birth_d.day))
            for curs in student["courses"]:
                curs_count[curs] += 1
        report_json["average_enrollment_age"] = round(age_all / report_json["total_students"], 1)
        report_json["students_per_course"] = dict(sorted(curs_count.items()))
        # print(report_json)
        json.dump(report_json, file_out, indent=2)
except FileNotFoundError:
    print(f"Файл {file_source} не найден.")
