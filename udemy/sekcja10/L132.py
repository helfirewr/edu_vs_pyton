# Zadanie - klasa do tworzenia pizzy
# Stworzysz teraz prostą klasę Pizza, która pozwoli na tworzenie
# obiektu pizzy z listą składników.
#
# 1) Zdefiniuj klasę Pizza z konstruktorem (__init__), który tworzy
#    atrybut `ingredients` (składniki), będący pustą listą na start.
# 2) Dodaj metodę `addIngredient`, która przyjmuje jeden parametr
#    (oprócz self) - składnik (ingredient) do dodania do pizzy.
#    Sprawdź, czy składnik jest typu str, jeśli tak - dodaj go do listy.
# 3) Dodaj metodę `showIngredients`, która wyświetla wszystkie
#    składniki pizzy.
# 4) Stwórz instancję klasy Pizza.
# 5) Dodaj składniki do pizzy używając metody `addIngredient`:
#    "ser", "pomidor", "pieczarki"
# 6) Wyświetl składniki pizzy wywołując metodę `showIngredients`.


class Pizza:
    def __init__(self) -> None:
        self.ingredients = []

    def addIngredient(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)
        else:
            print("Nieprawidłowe dane")

    def showIngredients(self):
        print("Skladniki:", self.ingredients)



pizza = Pizza()
pizza.addIngredient("ser")
pizza.addIngredient("pomidor")
pizza.addIngredient("pieczarki")

pizza.showIngredients()