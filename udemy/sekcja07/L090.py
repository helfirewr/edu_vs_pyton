# Zadanie: Kalkulator BMI z funkcją
#
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateBMI, która przyjmuje wagę w kilogramach i wzrost w centymetrach.
#    Funkcja powinna obliczać BMI i zwracać wartość BMI według wzoru:
#    weight / ((height / 100) ** 2)
# 2) Zdefiniuj funkcję classifyBMI, która przyjmuje wartość BMI i klasyfikuje ją
#    do odpowiedniego przedziału.
#    bmi < 18.5   z info:  Masz niedowagę.
#    bmi < 25   z info:  Twoja waga jest w normie.
#    bmi < 30   z info:  Masz nadwagę.
#    reszta wartości to: "Masz sporą nadwagę."
# 3) Poproś użytkownika o wprowadzenie wagi i wzrostu.
# 4) Wywołaj funkcję calculateBMI, aby obliczyć BMI na podstawie danych użytkownika.
# 5) Wywołaj funkcję classifyBMI, aby określić przedział BMI i wyświetlić odpowiedni komunikat.
#

def calculateBMI(weight, height):
    return weight / ((height / 100) ** 2 )

def classifyBMI(bmi):
    if bmi < 18.5:
        return "Masz niedowagę"
    elif bmi < 25:
        return "Twoja waga jest w normie"
    elif bmi < 30:
        return "Masz nadwagę"
    else:
        return "Masz sporą nadwagę"


weight = float(input("Podaj wagę w kg:"))
height = float(input("Podaj wzrost w cm:"))

bmi = calculateBMI(weight, height)

result = classifyBMI(bmi)
print(result)
