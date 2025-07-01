"""
1.  Счётчик экземпляров.
    Создайте класс User, представляющий пользователя.
    При создании должны указываться логин (username) и пароль (password).
    У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
    При каждом создании нового объекта User, счётчик должен увеличиваться.
    Добавьте метод get_total(), возвращающий количество пользователей.
    Проверьте, что счётчик работает.
Пример вывода:
Total users: 2
"""


class User:
    total_users = 0

    @classmethod
    def get_total(cls):
        print(f'Total users:', cls.total_users)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1


user_1 = User("user1", "password1")
user_2 = User("user2", "password2")
User.get_total()
user_3 = User("user3", "password3")
user_4 = User("user4", "password4")
user_5 = User("user5", "password5")
User.get_total()

print()

"""
2.  Проверка данных пользователя
    Доработайте класс User.
    Добавьте валидации полей при создании.
    Имя должно быть непустой строкой.
    Пароль должен быть строкой длиной не менее 5 символов.
    Если данные некорректны — выбрасывайте ValueError.
    Добавьте строковое представление объекта.
    Проверьте работу класса с разными значениями.
Пример вызова:
user1 = User("alice", "secret")
user2 = User("bob", "qwe")
Пример вывода:
User: alice
...
ValueError: Invalid password: 'qwe'.
"""


class UserUpd:
    total_users = 0

    def __init__(self, username, password):
        try:
            if not username or username.isspace():
                raise ValueError(f"Username is empty!")
            if len(password) < 5:
                raise ValueError(f"Invalid password: '{password}'")

            self.username = username
            self.password = password
            UserUpd.total_users += 1

        except ValueError as e:
            print(f"ValueError: {e}")

    def __repr__(self):
        return f"User(Name: {self.username!r}, Password={self.password!r})"

    def __str__(self):
        return f"User: {self.username}"

    @classmethod
    def get_total(cls):
        print(f'Total users:', cls.total_users)


# user1 = UserUpd("alice", "secret")
# user2 = UserUpd("bob", "qwerty")
# print(user1)
# print(repr(user2))
# user3 = UserUpd("bob-bad", "qwe")
# user4 = UserUpd(" ", "qwerty")
# user5 = UserUpd("", "qwerty")

users = [("alice", "secret"), ("bob", "qwerty"), ("bob-bad", "qwe"), (" ", "qwerty"), ("", "qwerty")]
for name, password in users:
    user = UserUpd(name, password)
    if user.__dict__:
        print(user)
        print(repr(user))
UserUpd.get_total()
