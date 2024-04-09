# Zadanie do wykonania:
# Wykorzystaj operatory logiczne (and, or, not) do sprawdzenia
# różnych warunków i wyświetl odpowiednie komunikaty w konsoli.
# 1) Sprawdź jednocześćnie, czy zmienna 'hoursWorked' z wartością 9 jest większa od 8 i czy
#    'projectFinished' z True jest True. Jeśli tak, wyświetl "Możesz iść do domu".
# 2) Sprawdź, czy temperatura 'temp' jako 35 jest mniejsza od 0 lub większa od 30.
#    Jeśli tak, wyświetl "Ekstremalne warunki pogodowe".
# 3) Użyj operatora not, aby sprawdzić, czy 'isHoliday' z False czy jest False.
#    Jeśli tak, wyświetl "Dziś jest dzień roboczy".
# 4) Użyj kombinacji operatorów, aby sprawdzić, czy 'errorsFound' z 12 jest
#    mniejsze od 10 i czy 'warnings' z 1 jest równe 0. Jeśli nie, wyświetl
#    "Sprawdź kod jeszcze raz".

hoursWorked = 9
projectFinished = True

if hoursWorked > 8 and projectFinished:
    print("Możesz iść do domu")


temp = 35
if temp < 0 or temp > 30:
    print("Ekstremlane warunki pogodowe")


isHoliday = False

if not isHoliday:
    print("Dziś jest dzień roboczy")