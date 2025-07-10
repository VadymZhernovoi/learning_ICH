"""
1. Электронное письмо.
    Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:
        sender — адрес отправителя
        recipient — адрес получателя
        subject — тема письма
        body — текст письма
        date — дата отправки
    Класс должен поддерживать:
        Сравнение писем по дате
        Преобразование письма в строку
        Получение длины текста письма
        Проверку на наличие текста в письме или не состоит ли текст только из пробелов
Пример использования:
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

Пример вывода:
From: alice@example.com
To: bob@example.com
Subject: Meeting
- Let's meet at 10am -

From: bob@example.com
To: alice@example.com
Subject: Report
-  -

Length: 18
Has text: True
Is newer: True
"""
from datetime import datetime
from functools import total_ordering

class DateFormatError(Exception):
    """Вызывается, если неправильно передана дата"""
    pass

@total_ordering
class Email:

    def __init__(self, sender:str, recipient:str, subject:str, body:str, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = Email.check_date(date) # чуть-чуть заморочился

    def __eq__(self, other):
        if not isinstance(other, Email):
            return NotImplemented
        return self.date == other.date

    def __lt__(self, other):
        if not isinstance(other, Email):
            return NotImplemented
        return self.date < other.date

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        # return not not self.body.strip()
        return bool(self.body.strip())

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -\n"

    @staticmethod
    def check_date(date):
        if isinstance(date, str):
            date_ret = 0
            formats = ["%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"]  # Добавьте другие форматы
            for format_d in formats:
                try:
                    date_ret = datetime.strptime(date, format_d)
                    return date_ret
                except ValueError:
                    pass
            if date_ret == 0:
                raise DateFormatError(f"Неправильный формат даты ({date})")
        elif isinstance(date, int):
            try:
                return datetime.strptime(str(date), "%Y%m%d")
            except ValueError:
                raise DateFormatError(f"Неправильный формат даты ({date})")
        elif isinstance(date, datetime):
            return date
        else:
            raise DateFormatError(f"Неправильный формат даты ({date})")

try:
    e0 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", 2024060)
    #e0 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", "2024-06.10")
except DateFormatError as e:
    print("Error:", e)
    
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", 20240610)
#e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Length:", len(e2))
print("Has text:", bool(e1))
print("Has text:", bool(e2))
print("Is newer:", e2 > e1)
print("Is older:", e2 < e1)

"""
2.  Класс для работы с деньгами.
    Создайте класс Money, в котором можно:
        складывать и вычитать объекты через операторы + и -
        выводить объект как строку в виде "$<amount>"
        при сложении и вычитании возвращается новый объект
        если вычитание приводит к отрицательному значению — вернуть 0
Пример использования: 
money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

Пример вывода: 
$150
$50
$0
"""


class Money:
    def __init__(self, amount:float):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        result = self.amount - other.amount
        return Money(result if result > 0 else 0)

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)
