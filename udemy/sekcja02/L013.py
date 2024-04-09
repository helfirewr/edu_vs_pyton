# 1. Wykorzystaj funkcję input() wbudowaną w python do
#    pobrania informacji od użytkownika z konsoli.
#    Poproś użytkownika o podanie imienia, nazwiska, miasta
#    Zapisz te informacje w zmiennych name, surname i city
# 2. Wyświetl w konsoli tekst podsumowujący pobrane dane:
#    "Nazywasz się Ania Kowalska i mieszkasz w mieście: Krk"

print("Wpisz imię:")
name = input()

print("Napisz nazwisko:")
surname = input()

print("Wpisz miasto:")
city = input()

print("Nazywasz się " + name + " " + surname + " i mieszkasz w mieście " + city)