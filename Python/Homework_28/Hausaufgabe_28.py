'''
1.  План по дням недели
    Напишите программу, которая помогает планировать дела.
    Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
    Данные:
    # Расписание дел на неделю
    weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
    }
    Пример ввода:
    Нажмите 'Enter' для получения плана:
    Monday: Gym, Work, Read book
    Нажмите 'Enter' для получения плана:
    Tuesday: Meeting, Work, Study Python
    ...
    Нажмите 'Enter' для получения плана:
    Sunday: Family time, Rest
    Нажмите 'Enter' для получения плана:
    Monday: Gym, Work, Read book
    Нажмите 'Enter' для получения плана: q
'''

# * - с возможностью изменять список задач на текущий день

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
    }
import itertools
from collections import defaultdict
def get_task(weekly_schedule : dict):
    return itertools.cycle(list(weekly_schedule.items()))
tasks = get_task(weekly_schedule)
day = ""
while True:
    if day:
        inp = input(f"Нажмите 'Enter' - получить новый план, либо введите: 'e' - изменить план на {day}, или 'q' - выход --> ", )
    else:
        inp = input(f"Нажмите 'Enter' - получить план или 'q' - выход --> ", )
    if inp not in ("", "e", "q"):
        print("Ошибка ввода! Может быть только 'e', 'q' или пусто.")
        continue
    if inp.lower() == 'q':
        break
    elif inp ==  'e':
        task = weekly_schedule[day]
        new_str = input(f"Hа {day} было запланировано: {", ".join(task)} \nВедите через запятую новые задачи --> ").strip()
        new_tasks = [t.strip() for t in new_str.split(",") if new_str.strip()]
        if not new_tasks:
            print("Ошибка! Неверно введены/отсутствуют новые задачи.")
            continue
        weekly_schedule = defaultdict()
        weekly_schedule[day] = new_tasks
        while True:  # чтобы дальше продолжить iter с этого числа
            d, t = next(tasks)
            if d == day:
                break
            weekly_schedule[d] = t
        tasks = get_task(weekly_schedule)
    day, task = next(tasks)
    print(f"{day}: {', '.join(task)}")

'''
2.  Объединение списков продуктов
    Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, 
    содержащий все продукты в нижнем регистре.
    Выведите содержимое генератора.
    Данные:
    fruits = ["Apple", "Banana", "Orange"]
    vegetables = ["Carrot", "Tomato", "Cucumber"]
    dairy = ["Milk", "Cheese", "Yogurt"]
    Пример вывода:
    apple
    banana
    orange
    carrot
    tomato
    cucumber
    milk
    cheese
    yogurt
'''
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]
from typing import Generator
def chain_list(*list: list[str]) -> Generator[str]:
    '''
    Принимает произвольное количество списков со строками и возвращает генератор,
    содержащий все строки в нижнем регистре.
    :param list: списки строк.
    :return: генератор, содержащий все строки в нижнем регистре.
    '''
    return (item.lower() for item in itertools.chain(*list))

result = chain_list(fruits,vegetables,dairy)
for item in result:
    print(item)

'''
3.  Комбинации одежды
    Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
    в формате "Clothe - Color - Size".
    Данные:
    clothes = ["T-shirt", "Jeans", "Jacket"]
    colors = ["Red", "Blue", "Black"]
    sizes = ["S", "M", "L"]
    Пример вывода:
    T-shirt - Red - S
    T-shirt - Red - M
    T-shirt - Red - L
    T-shirt - Blue - S
    ...
    Jacket - Black - L
'''
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def combine_list(*list: list[str]) -> list[str]:
    '''
    Принимает списки строк, а затем генерирует все возможные комбинации
    в формате "str1 - str2 - str3".
    :param list: списки строк.
    :return: Список строк со всеми возможными комбинациями строк.
    '''
    return [" - ".join(item) for item in itertools.product(*list)] # я так понял, что надо вернуть сгенерированный список, а не генератор
    # return (" - ".join(item) for item in itertools.product(*list))  # это возврат генератора

for item in combine_list(clothes, colors, sizes):
    print(item)