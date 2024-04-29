# Pracownicy w liście z zwiększoną pensją
# 1) Stwórz globalną zmienną employees, która jest pustą listą
# 2) Napisz funkcję addEmployee która przyjmuje email i salary, wewnątrz stwórz
#    słownik z tymi samymi parametrami. Następnie dodaj go do globalnej listy
#    employees stosując funkcję append np someList.append(newElement)
# 3) Wywołaj funkcję addEmployee dla trzech dowolnych pracowników
#    o pensjach: 6000, 8000 i 10000, wpisz dowolne maile
# 4) Dodaj funkcję increaseSalary z dwoma argumentami: employees i pctIncrease
#    Jako pierwszy argument będzie przekazywana lista pracowników, a do drugiego
#    wartość podwyżki np. 15  Przejdź po wszystkich pracownikach i zwiększ
#    pensję pracowników o przekazaną wartość procentową pctIncrease
# 5) Zwiększ pensje pracowników z funkcją increaseSalary o 20%, wyświetl
#    listę w terminalu


employees = []

def addEmployee(email, salary):
    e = {
        "email": email,
        "salary": salary
    }

    employees.append(e)


addEmployee("ania@test.com", 6000)
addEmployee("adam@test.com", 8000)
addEmployee("kasia@test.com", 10000)

# pctIncrease np 20
def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01

    for e in employees:
        e["salary"] *= 1 + pctIncrease


increaseSalary(employees, 20)
print(employees)

