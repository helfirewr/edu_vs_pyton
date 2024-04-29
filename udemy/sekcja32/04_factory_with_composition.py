# Wzorzec projektowy Fabryka z Kompozycją jest używany do tworzenia złożonych obiektów,
# które składają się z wielu mniejszych obiektów, tworząc relacje kompozycyjne między nimi.

# Zalety:
# 1. Większa elastyczność w tworzeniu skomplikowanych struktur obiektów.
# 2. Umożliwia oddzielenie procesu konstrukcji obiektu od jego reprezentacji.
# 3. Łatwiejsze zarządzanie zależnościami między komponentami.

# Wady:
# 1. Zwiększona złożoność systemu przez potrzebę zarządzania wieloma klasami.
# 2. Możliwość skomplikowania struktury, jeśli nie jest właściwie zaprojektowana.

from abc import ABC, abstractmethod

# Klasa bazowa dla elementów budynku
class BuildingComponent(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Konkretne komponenty
class Room(BuildingComponent):
    def display_info(self):
        return "Pokój"

class Window(BuildingComponent):
    def display_info(self):
        return "Okno"

class Door(BuildingComponent):
    def display_info(self):
        return "Drzwi"

# Klasa bazowa budynku
class Building(ABC):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def display_info(self):
        return ", ".join([component.display_info() for component in self.components])

# Konkretne fabryki
class HouseFactory:
    def create_building(self):
        house = Building()
        house.add_component(Room())
        house.add_component(Window())
        return house

class OfficeFactory:
    def create_building(self):
        office = Building()
        office.add_component(Room())
        office.add_component(Door())
        return office

# Funkcja do tworzenia budynku na podstawie typu
def create_building(building_type):
    if building_type == "house":
        factory = HouseFactory()
    elif building_type == "office":
        factory = OfficeFactory()
    else:
        raise ValueError("Nieznany typ budynku")
    return factory.create_building()

# Użycie wzorca Fabryka z Kompozycją
house = create_building("house")
print("Dom składa się z: " + house.display_info())

office = create_building("office")
print("Biuro składa się z: " + office.display_info())
