# Zadanie: Obliczanie pola powierzchni prostokąta
#
# Cel: Napisz program, który oblicza pole powierzchni prostokąta. Program
# powinien prosić użytkownika o wprowadzenie długości i szerokości prostokąta,
# a następnie obliczyć jego pole powierzchni.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateArea, która przyjmuje dwa parametry: length i width.
#    Funkcja ta powinna obliczać pole powierzchni prostokąta i zwracać wynik.
# 2) Poproś użytkownika o wprowadzenie długości prostokąta.
# 3) Poproś użytkownika o wprowadzenie szerokości prostokąta.
# 4) Wywołaj funkcję calculateArea z wprowadzonymi wartościami i przechowaj wynik.
# 5) Wyświetl wynik obliczeń użytkownikowi.
#

def calculateArea(length, width):
    return length * width

length = float(input("Wprowadź długość prostokąta:"))
width = float(input("Wprowadź szerokość prostokąta:"))

area = calculateArea(length, width)

print(area)
