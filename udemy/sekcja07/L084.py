# Zadanie: Wyświetlanie listy zakupów
#
# Cel: Napisz program, który tworzy i wyświetla listę zakupów na podstawie
#  wprowadzonych przez użytkownika produktów.
# Program nie będzie zwracał żadnej wartości, ale bezpośrednio wyświetli listę zakupów w konsoli.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję displayShoppingList, która przyjmuje jeden parametr: shoppingList.
#    Funkcja ta powinna wyświetlać wszystkie elementy listy zakupów, każdy element w nowej linii.
# 2) Stwórz pustą listę zakupów.
# 3) W pętli, poproś użytkownika o wprowadzenie nazw produktów do listy zakupów,
#    aż do wpisania słowa "koniec".
# 4) Po zakończeniu wprowadzania, wywołaj funkcję displayShoppingList, przekazując jej listę zakupów.
#

def displayShoppingList(shoppingList):
    print("Twoja list zakupów:")
    for item in shoppingList:
        print(" - ", item)


shoppingList = []

while True:
    product = input("Wpisz kolejny proukt do listy:")
    if product == "koniec":
        break
    shoppingList.append(product)

displayShoppingList(shoppingList)

