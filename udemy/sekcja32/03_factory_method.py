# Wzorzec projektowy Fabryka (Factory Method) jest używany do tworzenia obiektów w superklasie,
# ale umożliwia podklasom zmianę typu tworzonych obiektów.

# Zalety:
# 1. Oddzielenie logiki tworzenia obiektów od ich użycia.
# 2. Większa elastyczność i ponowne wykorzystanie kodu.
# 3. Łatwość wprowadzania nowych typów produktów do programu.

# Wady:
# 1. Może prowadzić do zwiększenia liczby klas w systemie.
# 2. Wymaga dodatkowej pracy przy dodawaniu nowych rodzajów produktów.

from abc import ABC, abstractmethod

# Klasa bazowa pojazdu
class Vehicle(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def display_info(self):
        pass

# Konkretne implementacje pojazdów
class Car(Vehicle):
    def display_info(self):
        return f"Samochód model {self.model}"

class Bike(Vehicle):
    def display_info(self):
        return f"Rower model {self.model}"

# Klasa bazowa fabryki
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, model):
        pass

# Konkretne fabryki
class CarFactory(VehicleFactory):
    def create_vehicle(self, model):
        return Car(model)

class BikeFactory(VehicleFactory):
    def create_vehicle(self, model):
        return Bike(model)

# Funkcja do tworzenia pojazdu na podstawie typu
def create_vehicle(vehicle_type, model):
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "bike":
        factory = BikeFactory()
    else:
        raise ValueError("Nieznany typ pojazdu")
    return factory.create_vehicle(model)

# Użycie wzorca Fabryka
car = create_vehicle("car", "Sedan")
print(car.display_info())  # Wyświetla informacje o samochodzie

bike = create_vehicle("bike", "Mountain")
print(bike.display_info())  # Wyświetla informacje o rowerze
