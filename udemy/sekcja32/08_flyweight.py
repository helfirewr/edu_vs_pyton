# Wzorzec projektowy Flyweight jest używany do efektywnego zarządzania dużą ilością
# obiektów, które mają wspólne właściwości, ograniczając zużycie pamięci.

# Zalety:
# 1. Zmniejsza liczbę obiektów, zmniejszając tym samym zużycie pamięci.
# 2. Umożliwia lepsze zarządzanie zasobami, gdy obiektów jest wiele.

# Wady:
# 1. Może komplikować kod, jeśli nie jest właściwie zarządzany.
# 2. W pewnych sytuacjach może prowadzić do problemów z wydajnością przy częstym dostępie
#    do współdzielonych obiektów.

class CarFlyweight:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self, vin):
        return f"{self.brand} {self.model}, Kolor: {self.color}, VIN: {vin}"

class CarFactory:
    _cars = {}

    def get_car(self, brand, model, color):
        key = (brand, model, color)
        if not key in self._cars:
            self._cars[key] = CarFlyweight(brand, model, color)
        return self._cars[key]

# Użycie wzorca Flyweight
factory = CarFactory()
car1 = factory.get_car("Toyota", "Corolla", "Czerwony")
car2 = factory.get_car("Toyota", "Corolla", "Czerwony")
car3 = factory.get_car("Ford", "Fiesta", "Niebieski")

print(car1.display_info("VIN12345"))
print(car2.display_info("VIN67890"))
print(car3.display_info("VIN54321"))

