"""
1.  Банковский счёт.
    Создайте класс BankAccount, описывающий банковский счёт.
    Объект должен хранить имя владельца и текущий баланс.
    Реализуйте методы:
    пополнение счёта
    снятие средств
    отображение баланса
    При попытке снять больше, чем есть на счёте, операция не должна выполняться.
    Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
Пример вывода:
Current balance: 150
Error: Amount must be positive.
Current balance: 150
Error: Not enough funds.
Current balance: 150
"""


class BankAccount:
    def __init__(self, name_owner: str, init_balance: float = None): # в условии не указано, должен ли баланс инициализироваться. Сделал так.
        self.name_owner = name_owner
        if init_balance:
            self.__current_balance = float(init_balance)
        else:
            self.__current_balance = 0

    def get_balance(self):
        print(f"Current balance: {round(self.__current_balance, 2)}")

    def deposit(self, amount: float = 0):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.__current_balance += amount

    def withdraw(self, amount: float = 0):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if amount > self.__current_balance:
            raise ValueError("Not enough funds.")
        self.__current_balance -= amount


acc_1 = BankAccount("Owner_1", 100.06)
acc_1.get_balance()
acc_1.deposit(500)
acc_1.get_balance()
try:
    acc_1.deposit(-100)
except ValueError as e:
    print(f"Error: {e}")
acc_1.get_balance()
try:
    acc_1.withdraw(601)
except ValueError as e:
    print(f"Error: {e}")
acc_1.get_balance()
try:
    acc_1.withdraw(-60)
except ValueError as e:
    print(f"Error: {e}")
acc_1.withdraw(20.03)
acc_1.get_balance()

acc_2 = BankAccount("Owner_2")
acc_2.get_balance()
acc_2.deposit(500)
acc_2.get_balance()

"""
2.  История операций
    Доработайте класс BankAccount.
    Каждая операция пополнения и снятия должна сохраняться в историю.
    История должна быть доступна через property history только для чтения.
    История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).
Пример вывода:
Current balance: 50
Operation history:
Deposit: 150
Withdraw: 100
"""


class BankAccountMod:
    def __init__(self, name_owner: str):
        self.name_owner = name_owner
        self.__current_balance = 0
        self.__history = []

    @property
    def current_balance(self):
        return self.__current_balance

    @current_balance.setter
    def current_balance(self, init_balance):
        self.__current_balance = init_balance
        self.__history.append(f"Set balance: {init_balance}")
        print(f"Balance set to: {self.__current_balance}")

    def deposit(self, amount: float = 0):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.__current_balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount: float = 0):
        if amount < 0:
            raise ValueError("Amount must be positive.")
        if amount > self.__current_balance:
            raise ValueError("Not enough funds.")
        self.__current_balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {round(self.__current_balance, 2)}")

    @property
    def history(self):
        return self.__history

def print_balance(balance: float=0):
    print(f"Current balance: {round(balance, 2)}")


print("*"*50)

acc_3 = BankAccountMod("Owner_3")

acc_3.current_balance = 654.99          # используем сеттер
print_balance(acc_3.current_balance)    # ... геттер
acc_3.show_balance()                    # или метод

acc_3.deposit(50)
try:
    acc_3.deposit(-100)
except ValueError as e:
    print(f"Error: {e}")
print_balance(acc_3.current_balance)
try:
    acc_3.withdraw(601)
except ValueError as e:
    print(f"Error: {e}")
print_balance(acc_3.current_balance)
try:
    acc_3.withdraw(-60)
except ValueError as e:
    print(f"Error: {e}")
acc_3.withdraw(20.03)
print_balance(acc_3.current_balance)
acc_3.current_balance = 9999.99
print_balance(acc_3.current_balance)

print("Operation history:")
for h in acc_3.history:
    print(f"\t{h}")
# print(acc_3.name_owner)
