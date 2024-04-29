# Wzorzec projektowy Fabryka jest używany do tworzenia obiektów w superklasie, ale umożliwia
# podklasom zmianę typu tworzonych obiektów.

# Zalety:
# 1. Oddzielenie logiki tworzenia obiektu: Ułatwia zarządzanie tworzeniem obiektów poprzez oddzielenie
#    logiki tworzenia od głównej logiki aplikacji.
# 2. Większa elastyczność: Umożliwia dodawanie nowych typów produktów bez zmiany istniejącego kodu klienta.
# 3. Łatwe wprowadzanie nowych typów produktów: Można łatwo wprowadzić nowe klasy produktów.

# Wady:
# 1. Złożoność systemu: Może zwiększyć złożoność systemu, ponieważ dodaje dodatkowe klasy.
# 2. Wymaga dodatkowych klas: Każdy nowy typ produktu wymaga nowej podklasy.

# Definiowanie interfejsu fabryki
from abc import ABC, abstractmethod

# Abstrakcyjna klasa fabryki pojazdów
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, vehicle_type):
        pass

# Implementacja konkretnych fabryk
class CarFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        return Car(vehicle_type)

class TruckFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
        return Truck(vehicle_type)

# Abstrakcyjna klasa pojazdu
class Vehicle(ABC):
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    @abstractmethod
    def display_info(self):
        pass

# Konkretne implementacje pojazdów
class Car(Vehicle):
    def display_info(self):
        return f"Samochód typu {self.vehicle_type}"

class Truck(Vehicle):
    def display_info(self):
        return f"Ciężarówka typu {self.vehicle_type}"

# Użycie wzorca Fabryka
car_factory = CarFactory()
car = car_factory.create_vehicle("sedan")
print(car.display_info())  # Wyświetla "Samochód typu sedan"

truck_factory = TruckFactory()
truck = truck_factory.create_vehicle("ciężarówka")
print(truck.display_info())  # Wyświetla "Ciężarówka typu ciężarówka"
