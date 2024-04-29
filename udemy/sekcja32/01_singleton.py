from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Singleton to wzorzec projektowy służący do zapewnienia, że klasa ma tylko jedną instancję
# i zapewnia globalny punkt dostępu do tej instancji. Jest często stosowany do zarządzania 
# zasobami, takimi jak połączenia z bazą danych.

# Zalety:
# 1. Kontrolowana instancja: Zapewnia, że istnieje tylko jedna instancja klasy.
# 2. Oszczędność zasobów: Przydatny do zarządzania zasobami, które są kosztowne
#    do tworzenia i niszczą, np. połączenia z bazą danych.
# 3. Łatwy dostęp: Umożliwia globalny dostęp do swojej instancji.

# Wady:
# 1. Globalny stan: Przechowuje stan globalnie, co może być problematyczne w 
#    środowisku wielowątkowym.
# 2. Trudność w testowaniu: Może być trudniejszy do przetestowania, ponieważ
#    zachowanie zależy od jednej instancji.
# 3. Elastyczność: Może ograniczać elastyczność, ponieważ kod zależy od konkretnej
#    implementacji klasy.

class DatabaseConnection:
    _instance = None  # Zmienna klasowa przechowująca instancję singletona
    _engine = None  # Zmienna klasowa przechowująca silnik bazy danych
    _session = None  # Zmienna klasowa przechowująca sesję bazy danych

    def __new__(cls, uri):
        if cls._instance is None:  # Sprawdza, czy instancja już istnieje
            # Tworzy nową instancję, jeśli nie istnieje
            cls._instance = super(DatabaseConnection, cls).__new__(cls)  
            # Tworzy nowy silnik bazy danych z podanego URI
            cls._engine = create_engine(uri)  
            # Tworzy sesję związane z silnikiem
            cls._session = sessionmaker(bind=cls._engine)()  
        return cls._instance  # Zwraca istniejącą instancję singletona

    def get_session(self):
        return self._session  # Zwraca sesję do interakcji z bazą danych

    def close_connection(self):
        self._session.close()  # Zamyka sesję bazy danych
        self._engine.dispose()  # Zwalnia zasoby silnika bazy danych

# Przykład użycia Singletona
uri = 'postgresql+psycopg2://postgres:admin12345@localhost/sqlalchemy'  # URI bazy danych
db1 = DatabaseConnection(uri)  # Tworzy pierwszą instancję połączenia
session1 = db1.get_session()  # Pobiera sesję z pierwszej instancji

db2 = DatabaseConnection(uri)  # Tworzy drugą instancję połączenia
session2 = db2.get_session()  # Pobiera sesję z drugiej instancji

# Sprawdzenie, czy obie instancje są takie same
print(db1 is db2)  # Powinno wypisać True, ponieważ obie zmienne odnoszą się do tej samej instancji
