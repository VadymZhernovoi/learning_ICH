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

tasks = itertools.cycle(list(weekly_schedule.items()))

while True:
    if input("Нажмите 'Enter' для получения плана: "):
        break
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
from typing import Iterable, Generator
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