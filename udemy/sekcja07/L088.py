# Zadanie na przekazanie danych funkcji przez wartość
# 1) Napisz funkcję increaseSalary z dwoma parametrami
#    liczbowymi: money oraz bonus
# 2) W funkcji podnieś wartość money o 20%.
#    Następnie zwróć sumę money i bonus.
# 3) Stwórz zmienną salary poza funkcją o wartości 5000
# 4) Wywołaj funkcję increaseSalary przekazując jako
#    argument salary oraz 1000 jako bonus. Zachowaj
#    zwracaną wartość w zmiennej newSalary.
# 4) Pokaż w konsoli wartości: salary i newSalary,
#    ponieważ przekazywane dane są niemutowalne to salary
#    musi mieć wartość 5k, a newSalary odpowiednio większą
#    według implementacji funkcji.

def increaseSalary(money, bonus):
    return money*1.2, bonus

salary=5000

newSalary=increaseSalary(money=salary, bonus=1000)
print(salary)
print(newSalary)