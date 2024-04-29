
# 1. Napisz funkcję findLargest która przyjmuje
#    dwie liczby jako parametry num1 i num2.
#    Funkcja musi pokazać w konsoli informację,
#    która liczba jest większa oraz jej wartość.
#    np: "num1 jest większą liczbą: 12" lub, że obie
#    liczby są równe.
#    Pamiętaj aby użyć if elif oraz else.
# 2. Dodatkowo funkcja zwraca większą liczbę dzięki return
# 3. Sprawdź funkcję przekazując wartości 3 i 10,
#    pokaż w konsoli zwróconą wartość z funkcji
# 4. W ten sam sposób sprawdź funkcję dla 12 i 7

def findLargest(num1, num2):
    if (num1 > num2):
        print("num1 jest większe:", num1)
        return num1
    elif (num2 > num1):
        print("num2 jest większe", num2)
        return num2
    else:
        print("Obie liczby są równe o wartości:", num1)
        return num1

v1 = findLargest(3, 10)
print("Wynik wywołania:", v1)

v2 = findLargest(12, 7)
print("Wynik wywołania:", v2)
