# Zadanie: Tworzenie listy kwadratów liczb
#
# Cel: Napisz program, który utworzy listę zawierającą kwadraty liczb
# od 1 do N, gdzie N jest wartością wprowadzoną przez użytkownika.
# Na koniec program powinien wyświetlić utworzoną listę.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby N.
# 2) Użyj pętli for wraz z funkcją range() do wygenerowania liczb od 1 do N.
# 3) Dla każdej liczby z tego zakresu, oblicz jej kwadrat i dodaj do listy.
#     Pamiętaj że kwadrat liczby możesz zapisać z ** czyli np  result = 2 ** 2
# 4) Po zakończeniu pętli, wyświetl listę zawierającą kwadraty liczb.
# 5) Sprawdź za pomocą instrukcji if, czy lista nie jest pusta przed wyświetleniem.
#
# czyli np dla podanej wartości w konsoli: 3 rezultat będzie:
# Podaj liczbę N: 3
# Lista kwadratów liczb od 1 do N: [1, 4, 9]
# Rozwiązanie:

N = int(input("Wprowadź liczbę elementów:"))

squares_list = []

for number in range(1, N + 1):
    squares_list.append(number ** 2)

if squares_list:
    print("Lista kwadratów liczb od 1 do N:", squares_list)
else:
    print("Lista jest pusta")


