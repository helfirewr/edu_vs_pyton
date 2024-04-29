import psycopg2

# Wzorzec projektowy Factory with Composition jest używany do tworzenia obiektów,
# gdzie fabryka deleguje tworzenie składników do innych fabryk.

# Zalety:
# 1. Umożliwia tworzenie skomplikowanych obiektów z różnymi konfiguracjami.
# 2. Ułatwia zarządzanie procesem tworzenia obiektów.
# 3. Zapewnia elastyczność w tworzeniu różnych wariantów obiektów.

# Wady:
# 1. Może prowadzić do skomplikowanego kodu ze względu na wiele zaangażowanych klas.
# 2. Wymaga dokładnego planowania struktury klas.

# Nawiązywanie połączenia z bazą danych
conn = psycopg2.connect(dbname="py_test", user="postgres", password="admin12345", host="localhost")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS consoles;")
cur.execute("""
CREATE TABLE consoles (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    model VARCHAR(50),
    features VARCHAR(255)
);
""")
conn.commit()

class ConsoleFactory:
    def create_console(self, model):
        raise NotImplementedError

class PlayStationFactory(ConsoleFactory):
    def create_console(self, model):
        return PlayStation(model)

class XboxFactory(ConsoleFactory):
    def create_console(self, model):
        return Xbox(model)

class Console:
    def __init__(self, type, model, features):
        self.type = type
        self.model = model
        self.features = features

    def save_to_db(self):
        cur.execute("INSERT INTO consoles (type, model, features) VALUES (%s, %s, %s) RETURNING id;",
                    (self.type, self.model, self.features))
        console_id = cur.fetchone()[0]
        conn.commit()
        return console_id

    def display_info(self):
        return f"{self.type} {self.model}: {self.features}"

class PlayStation(Console):
    def __init__(self, model):
        features = "Blu-ray, VR support"
        super().__init__("PlayStation", model, features)

class Xbox(Console):
    def __init__(self, model):
        features = "Game Pass, Backward compatibility"
        super().__init__("Xbox", model, features)

# Tworzenie fabryk
ps_factory = PlayStationFactory()
xbox_factory = XboxFactory()

# Tworzenie konsol
ps5 = ps_factory.create_console("PS5")
ps5_id = ps5.save_to_db()
print(ps5.display_info())

xbox_series_x = xbox_factory.create_console("Xbox Series X")
xbox_series_x_id = xbox_series_x.save_to_db()
print(xbox_series_x.display_info())

# Zamykanie połączenia z bazą danych
cur.close()
conn.close()
