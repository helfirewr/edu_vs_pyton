import psycopg2

# Wzorzec projektowy Fabryka jest używany do tworzenia obiektów w superklasie, ale umożliwia
# podklasom zmianę typu tworzonych obiektów.

# Zalety:
# 1. Oddzielenie logiki tworzenia obiektu: Ułatwia zarządzanie tworzeniem obiektów.
# 2. Większa elastyczność: Umożliwia dodawanie nowych typów produktów.
# 3. Łatwe wprowadzanie nowych typów produktów.

# Wady:
# 1. Złożoność systemu: Może zwiększyć złożoność systemu.
# 2. Wymaga dodatkowych klas: Każdy nowy typ produktu wymaga nowej podklasy.

# Nawiązywanie połączenia z bazą danych
conn = psycopg2.connect(
    dbname="py_test",
    user="postgres",
    password="admin12345",
    host="localhost"
)
cur = conn.cursor()

# Tworzenie tabeli pojazdów
cur.execute("""
    DROP TABLE IF EXISTS vehicles;
    CREATE TABLE vehicles (
        id SERIAL PRIMARY KEY,
        vehicle_type VARCHAR(50),
        description VARCHAR(255)
    );
""")
conn.commit()

class VehicleFactory:
    def create_vehicle(self, vehicle_type, description):
        raise NotImplementedError("Metoda create_vehicle musi być zaimplementowana w podklasie.")

class CarFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type, description):
        return Car(vehicle_type, description)

class TruckFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type, description):
        return Truck(vehicle_type, description)

class Vehicle:
    def __init__(self, vehicle_type, description):
        self.vehicle_type = vehicle_type
        self.description = description

    def save_to_db(self):
        cur.execute("INSERT INTO vehicles (vehicle_type, description) VALUES (%s, %s) RETURNING id;",
                    (self.vehicle_type, self.description))
        vehicle_id = cur.fetchone()[0]
        conn.commit()
        return vehicle_id

    def display_info(self):
        raise NotImplementedError

class Car(Vehicle):
    def display_info(self):
        return f"Samochód typu {self.vehicle_type}, Opis: {self.description}"

class Truck(Vehicle):
    def display_info(self):
        return f"Ciężarówka typu {self.vehicle_type}, Opis: {self.description}"

# Tworzenie fabryk
car_factory = CarFactory()
truck_factory = TruckFactory()

# Tworzenie pojazdów
car = car_factory.create_vehicle("Sedan", "Wygodny sedan rodzinny")
car_id = car.save_to_db()
print(car.display_info())

truck = truck_factory.create_vehicle("Ciężarówka", "Ciężarówka do transportu towarów")
truck_id = truck.save_to_db()
print(truck.display_info())

