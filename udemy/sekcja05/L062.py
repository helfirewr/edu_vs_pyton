# Wyświetlenie elementów od końca z pętlą while
# 1) Stwórz listę elementów : Ania, Ola, Kasia, Daniel
# 2) Zapisz zmienną i od której w każdej iteracji pętli odejmiesz 1, to indeks
#    elementu w liście. Wpisz wartość początkową jako ostatni indeks listy
#    czyli element "Daniel"
# 3) W pętli while sprawdź czy i jest większe lub równe zero
#    Pobierz imię z listy z użyciem numeru indeksu w i, wyświetl je w konsoli.
#    Zmień wartość zmiennej i

names = ["Ania", "Ola", "Kasia", "Daniel"]

i = len(names) - 1

while i >= 0:
    person = names[i]
    print(person)
    i -= 1