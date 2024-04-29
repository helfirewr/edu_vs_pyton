# Wzorzec projektowy Builder jest używany do tworzenia skomplikowanych obiektów krok po kroku,
# oddzielając konstrukcję obiektu od jego reprezentacji.

# Zalety:
# 1. Większa kontrola nad procesem konstrukcji.
# 2. Umożliwia tworzenie różnych reprezentacji tego samego obiektu.
# 3. Dobre rozwiązanie, gdy obiekt musi być tworzony w wielu krokach.

# Wady:
# 1. Zwiększenie złożoności kodu przez konieczność tworzenia dodatkowych klas.
# 2. Może być przeładowany, gdy istnieją różne warianty obiektów z wieloma parametrami.

class PizzaBuilder:
    def __init__(self):
        self.topping = []
        self.size = "medium"

    def add_topping(self, topping):
        self.topping.append(topping)
        return self

    def set_size(self, size):
        self.size = size
        return self

    def build(self):
        return Pizza(self)

class Pizza:
    def __init__(self, builder):
        self.topping = builder.topping
        self.size = builder.size

    def display_info(self):
        toppings = ', '.join(self.topping) if self.topping else "bez dodatków"
        return f"Pizza {self.size} z {toppings}"

# Użycie wzorca Builder
builder = PizzaBuilder()
pizza = builder.set_size("duża").add_topping("ser").add_topping("pieczarki").build()
print(pizza.display_info())  # Wyświetla informacje o pizzy
