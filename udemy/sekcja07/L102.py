# Zadanie: Zarządzanie stanem konta użytkownika
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcje do modyfikacji tego stanu i wyświetlania go.
#
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną accountBalance z wartością początkową 0.
# 2) Napisz funkcję addFunds, która przyjmuje kwotę do dodania do konta.
#    Funkcja ta powinna modyfikować globalną zmienną accountBalance.
# 3) Napisz funkcję withdrawFunds, która przyjmuje kwotę do wypłaty z konta.
#    Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję displayBalance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję.
#
# Rozwiązanie:

accountBalance = 0

def addFunds(amount):
    global accountBalance
    accountBalance += amount
    print("Dodano środki:", amount)

def withdrawFunds(amount):
    global accountBalance
    if amount > accountBalance:
        print("Niewystarczające środki na koncie")
    else:
        accountBalance -= amount
        print("Wypłacono środki w kwocie:", amount)

def displayBalance():
    global accountBalance
    print("Stan konta:", accountBalance)

while True:
    action = input("Wybierz działanie: dodaj, wypłać, stan, koniec: ").lower()
    if action == "koniec":
        break
    elif action == "dodaj":
        amount = float(input("Podaj kwotę środków:"))
        addFunds(amount)
    elif action == "wypłać":
        amount = float(input("Podaj kwotę środków:"))
        withdrawFunds(amount)
    elif action == "stan":
        displayBalance()
    else:
        print("Nieznane działanie")











