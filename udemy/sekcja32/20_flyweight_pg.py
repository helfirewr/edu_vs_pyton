import psycopg2

# Wzorzec projektowy Flyweight jest używany do efektywnego zarządzania dużą liczbą małych obiektów.

# Zalety:
# 1. Oszczędność pamięci poprzez współdzielenie stanu między wieloma obiektami.
# 2. Zmniejszenie liczby tworzonych obiektów.

# Wady:
# 1. Zwiększenie złożoności kodu.
# 2. Trudność w zarządzaniu współdzielonym stanem.

conn = psycopg2.connect(dbname="py_test", user="postgres", password="admin12345", host="localhost")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS computers;")
cur.execute("""
CREATE TABLE computers (
    id SERIAL PRIMARY KEY,
    model VARCHAR(50),
    cpu VARCHAR(50),
    ram VARCHAR(50),
    storage VARCHAR(50)
);
""")
conn.commit()

class ComputerFlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ComputerFlyweight(key)
        return self._flyweights[key]

class ComputerFlyweight:
    def __init__(self, key):
        self.key = key
        self.model, self.cpu, self.ram, self.storage = key.split(':')

    def save_to_db(self):
        cur.execute("INSERT INTO computers (model, cpu, ram, storage) VALUES (%s, %s, %s, %s) RETURNING id;",
                    (self.model, self.cpu, self.ram, self.storage))
        computer_id = cur.fetchone()[0]
        conn.commit()
        return computer_id

    def display_info(self):
        return f"Model: {self.model}, CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"

# Użycie wzorca Flyweight
factory = ComputerFlyweightFactory()
computer1 = factory.get_flyweight("GamingPC:Intel i9:32GB:1TB SSD")
computer_id1 = computer1.save_to_db()
print(computer1.display_info())

computer2 = factory.get_flyweight("OfficePC:Intel i5:16GB:500GB SSD")
computer_id2 = computer2.save_to_db()
print(computer2.display_info())

computer3 = factory.get_flyweight("GamingPC:Intel i9:32GB:1TB SSD")
computer_id3 = computer3.save_to_db()
print(computer3.display_info())

# Sprawdzenie, czy computer1 i computer3 są tym samym flyweight
print(computer1 is computer3)  # Powinno wypisać True

