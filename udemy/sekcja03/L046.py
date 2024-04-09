# Zadanie do wykonania:
# Wykorzystaj operatory przynależności (in, not in) do sprawdzenia
# obecności elementów w kolekcjach i użycie instrukcji warunkowej if.
# 1) Sprawdź, czy liczba 7 znajduje się w liście 'numbers' i wyświetl odpowiedni komunikat.
# 2) Sprawdź, czy ciąg znaków "kot" nie znajduje się w tuple 'animals' i wyświetl odpowiedni komunikat.
# 3) Stwórz słownik 'user' z kluczami 'name' i 'age'. Sprawdź, czy klucz 'name' znajduje się w słowniku.
# 4) Jeśli w liście 'numbers' jest liczba 3, zwiększ jej wartość o 2 i wyświetl nową listę.
#    Użyj pętli for i instrukcji warunkowej if.

# Rozwiązanie:
numbers = [0,1,2,3,4,5]

# Sprawdzenie obecności liczby 7 w liście
if 7 in numbers:
    print("Liczba 7 znajduje się w liście.")
else:
    print("Liczba 7 nie znajduje się w liście.")

animals = ("pies", "kot", "ryba")

# Sprawdzenie nieobecności ciągu "kot" w tuple
if "kot" not in animals:
    print("Ciąg 'kot' nie znajduje się w tuple.")
else:
    print("Ciąg 'kot' znajduje się w tuple.")

user = {'name': 'Jan', 'age': 25}

# Sprawdzenie obecności klucza 'name' w słowniku
if 'name' in user:
    print("Klucz 'name' znajduje się w słowniku.")

# Zwiększenie wartości liczby 3 o 2, jeśli znajduje się w liście
for i in range(len(numbers)):
    if numbers[i] == 3:
        numbers[i] += 2

print("Nowa lista: ", numbers)