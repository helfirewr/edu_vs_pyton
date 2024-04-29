# Zadanie: Obliczanie ostatecznej ceny produktu po rabacie
#
# Cel: Napisz program, który oblicza ostateczną cenę produktu po zastosowaniu rabatu.
# Program powinien prosić użytkownika o wprowadzenie ceny początkowej produktu
# oraz wielkości rabatu w procentach, a następnie obliczyć i wyświetlić cenę końcową.
#
# Kroki do wykonania:
# 1) Napisz funkcję calculateFinalPrice, która przyjmuje dwa parametry:
#    initialPrice (cena początkowa produktu) oraz discount (rabat w procentach).
# 2) W funkcji oblicz cenę produktu po rabacie i zwróć tę wartość.
# 3) Poproś użytkownika o wprowadzenie ceny początkowej produktu oraz wielkości rabatu.
# 4) Wywołaj funkcję calculateFinalPrice z wprowadzonymi wartościami i przechowaj wynik.
# 5) Wyświetl ostateczną cenę produktu.
#


def calculateFinalPrice(initialPrice, discount):
    discountAmount = initialPrice * (discount / 100)
    finalPrice = initialPrice - discountAmount
    return finalPrice

initialPrice = float(input("Podaj cenę początkową produktu:"))
discount = float(input("Podaj wielkość tabatu produktu w procentach:"))

finalPrice = calculateFinalPrice(initialPrice, discount)
print("Cena po rabacie:", finalPrice)
