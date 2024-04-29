# Importowanie modułu 're', który jest używany do pracy z wyrażeniami
# regularnymi w Pythonie.
import re

# Definiowanie prostego wzorca regex do znalezienia litery 'a' w tekście.
# Zmienna 'pattern' przechowuje skompilowane wyrażenie regularne.
# Funkcja re.compile() kompiluje wyrażenie regularne do obiektu wzorca,
# który może być następnie użyty do wyszukiwania dopasowań w tekście.
pattern = re.compile('a')

# Przeszukujemy łańcuch tekstowy "apple" w poszukiwaniu wzorca zdefiniowanego w 'pattern'.
# Metoda 'search' przeszukuje tekst i zwraca pierwsze znalezione
# dopasowanie jako obiekt Match.
# Jeśli wzorzec nie zostanie znaleziony, 'search' zwraca None.
# 'search' jest przydatny, gdy interesuje nas tylko pierwsze wystąpienie wzorca.
match = pattern.search("apple")

# Sprawdzamy, czy znaleziono dopasowanie.
# Jeśli 'match' nie jest None, oznacza to, że znaleziono dopasowanie.
# W przeciwnym razie, jeśli 'match' jest None, wzorzec nie został znaleziony w tekście.
if match:
    print("Znaleziono dopasowanie.")
else:
    print("Nie znaleziono dopasowania.")

# Wyświetlamy szczegółowe informacje o znalezionym dopasowaniu, jeśli istnieje.
# 'match.group()' zwraca pasujący fragment tekstu.
# 'match.start()' i 'match.end()' zwracają indeksy początku
# i końca dopasowanego fragmentu w tekście.
# Te metody są przydatne, gdy chcemy wiedzieć, gdzie dokładnie
# w tekście znajduje się dopasowanie.
if match:
    print(f"Dopasowany fragment: {match.group()}")
    print(f"Indeks początku dopasowania: {match.start()}")
    print(f"Indeks końca dopasowania: {match.end()}")

# Użycie metody 'findall' do znalezienia wszystkich dopasowań wzorca w tekście.
# Ta metoda zwraca listę wszystkich dopasowanych fragmentów.
# Jest przydatna, gdy chcemy znaleźć wszystkie wystąpienia wzorca w tekście.
all_matches = pattern.findall("banana")

# Wyświetlamy listę wszystkich dopasowań.
print("Wszystkie dopasowania:", all_matches)

# Dodatkowo, używamy 'finditer' do znalezienia wszystkich dopasowań wraz z ich indeksami.
# 'finditer' zwraca iterator zawierający obiekty Match dla każdego dopasowania.
# To jest przydatne, gdy chcemy mieć szczegółowe informacje o każdym dopasowaniu,
# w tym indeksy jego początku i końca w tekście.
for match in pattern.finditer("banana"):
    print(f"Dopasowany fragment: {match.group()}, ind start: {match.start()}, ind end: {match.end()}")
