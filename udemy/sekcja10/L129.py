# Zadanie - zarządzanie kontem użytkownika
# W tym zadaniu stworzysz prostą klasę reprezentującą konto użytkownika.
# Będziesz zarządzać podstawowymi informacjami o użytkowniku oraz umożliwić zmianę hasła.
#
# 1) Stwórz klasę User, która w konstruktorze przyjmuje dwa parametry:
#    username (nazwa użytkownika) i password (hasło). Zapisz te wartości jako atrybuty obiektu.
# 2) Dodaj metodę changePassword, która przyjmuje dwa argumenty:
#    oldPassword (stare hasło) i newPassword (nowe hasło). Sprawdź, czy stare hasło
#    zgadza się z obecnym hasłem użytkownika. Jeśli tak, zmień hasło na nowe.
# 3) Stwórz instancję klasy User z przykładowym użytkownikiem.
# 4) Spróbuj zmienić hasło użytkownika za pomocą metody changePassword.
#    Najpierw użyj nieprawidłowego starego hasła, a następnie prawidłowego.


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.newPassword = newPassword
            print("Hasło zostało zmienione")
        else:
            print("Nieprawidłowe dane")

user = User("adamkowalski", "admin12345")
user.changePassword("dfgsuydfg", "dfdfsdfsdf")
user.changePassword("admin12345", "newpassword12345")