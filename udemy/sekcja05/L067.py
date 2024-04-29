# 1) Stwórz krotkę z wartościami od 1 do 10
# 2) Zrób pętle for in z krotką i wyświetl w konsoli
#    tylko parzyste liczby. Skorzytaj z instrukcji
#    warunkowej if oraz operatora % zwracającego resztę
#    z dzielenia. Jeśli reszta z dzielenia przez 2
#    będzie równa 0 to nie ma reszty, tym samym liczba
#    jest parzysta

data = (1,2,3,4,5,6,7,8,9,10)

for v in data:
    if v % 2 == 0:
        print(v, "to liczba parzysta")