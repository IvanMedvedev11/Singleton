import json
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
class PasswordManager(Singleton):
    def __init__(self):
        self.database = []
        self.state = False
    def get_database(self, filename):
        with open(filename, 'r') as file:
            self.database = json.load(file)
    def sign_up(self, login, password, e_mail):
        for user in self.database:
            if login == user['login']:
                print("Пользователь уже существует")
                break
        else:
            self.database.append({"login": login, "password": password, "e-mail": e_mail})
            self.state = True
            print("Вы успешно зарегистрированы")
    def sign_in(self, login, password):
        for user in self.database:
            if login == user["login"]:
                if password == user["password"]:
                    self.state = True
                    print("Вы успешно авторизованы")
                else:
                    print("Неверный пароль")
                break
        else:
            print("Пользователя не существует")
    def new_login(self, login, new_login):
        for i in range(len(self.database)):
            if login == self.database[i]["login"]:
                self.database[i]["login"] = new_login
                print("Логин успешно изменен")
                break
    def new_password(self, login, new_password):
        for i in range(len(self.database)):
            if login == self.database[i]["login"]:
                self.database[i]["password"] = new_password
                print("Пароль успешно изменен")
                break
    def new_email(self, login, new_email):
        for i in range(len(self.database)):
            if login == self.database[i]["login"]:
                self.database[i]["e-mail"] = new_email
                print("E-mail успешно изменен")
                break
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.database, file, indent=4)
manager = PasswordManager()
manager.get_database("password.json")
choose1 = input("1. Войти 2. Зарегистрироваться: ")
if choose1 == "1":
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    manager.sign_in(login, password)
elif choose1 == "2":
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    e_mail = input("Введите e-mail: ")
    manager.sign_up(login, password, e_mail)
if manager.state == True:
    choose2 = input("1. Сменить логин 2. Сменить пароль 3. Сменить e-mail 4. Ничего не делать: ")
    if choose2 == "1":
        new_login = input("Введите новый логин: ")
        manager.new_login(login, new_login)
    elif choose2 == "2":
        new_password = input("Введите новый пароль: ")
        manager.new_password(login, new_password)
    elif choose2 == "3":
        new_email = input("Введите новый e-mail: ")
        manager.new_email(login, new_email)
manager.save_to_file("password.json")
