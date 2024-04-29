import psycopg2

# Wzorzec projektowy Builder jest używany do tworzenia złożonych obiektów krok po kroku.

# Zalety:
# 1. Oddzielenie konstrukcji złożonego obiektu od jego reprezentacji.
# 2. Większa kontrola nad procesem konstrukcji.
# 3. Umożliwia tworzenie różnych reprezentacji tego samego obiektu.

# Wady:
# 1. Zwiększenie liczby klas: Każdy różny typ produktu wymaga oddzielnego buildera.
# 2. Kompleksowość kodu: Kod może stać się skomplikowany, jeśli obiekt ma wiele części.

conn = psycopg2.connect(dbname="py_test", user="postgres", password="admin12345", host="localhost")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS computer_sets;")
cur.execute("""
CREATE TABLE computer_sets (
    id SERIAL PRIMARY KEY,
    cpu VARCHAR(50),
    gpu VARCHAR(50),
    ram VARCHAR(50),
    storage VARCHAR(50)
);
""")
conn.commit()

class ComputerSetBuilder:
    def set_cpu(self, cpu):
        raise NotImplementedError

    def set_gpu(self, gpu):
        raise NotImplementedError

    def set_ram(self, ram):
        raise NotImplementedError

    def set_storage(self, storage):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

class GamingComputerBuilder(ComputerSetBuilder):
    def __init__(self):
        self.computer = {"cpu": "", "gpu": "", "ram": "", "storage": ""}

    def set_cpu(self, cpu):
        self.computer["cpu"] = cpu
        return self

    def set_gpu(self, gpu):
        self.computer["gpu"] = gpu
        return self

    def set_ram(self, ram):
        self.computer["ram"] = ram
        return self

    def set_storage(self, storage):
        self.computer["storage"] = storage
        return self

    def build(self):
        cur.execute("INSERT INTO computer_sets (cpu, gpu, ram, storage) VALUES (%s, %s, %s, %s) RETURNING id;",
                    (self.computer["cpu"], self.computer["gpu"], self.computer["ram"], self.computer["storage"]))
        computer_id = cur.fetchone()[0]
        conn.commit()
        return computer_id

# Użycie wzorca Builder
builder = GamingComputerBuilder()
builder.set_cpu("Intel Core i9").set_gpu("NVIDIA RTX 3080").set_ram("32GB").set_storage("1TB SSD")
computer_id = builder.build()
print(f"Zbudowano zestaw komputerowy o ID: {computer_id}")
