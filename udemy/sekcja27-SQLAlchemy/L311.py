
# pip install sqlalchemy
# utwór zbazę sqlalchemy w pgadmin

from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import declarative_base, Session

# Parametry połączenia z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'

# Nawiązywanie połączenia z bazą danych
engine = create_engine(DATABASE_URI)  # Tworzenie silnika połączenia z bazą danych

# Tworzenie klasy bazowej
# Declarative base to klasa bazowa dla wszystkich modeli tabel, pozwala na deklaratywne definiowanie struktury tabel.
Base = declarative_base()

# Definiowanie modelu tabeli
# Klasa ExampleTable dziedziczy po Base i reprezentuje tabelę w bazie danych.
class ExampleTable(Base):
    __tablename__ = 'example_table'  # Nazwa tabeli w bazie danych
    id = Column(Integer, primary_key=True)  # Definicja kolumny 'id'
    name = Column(String)  # Definicja kolumny 'name'
    description = Column(String)  # Definicja kolumny 'description'

# Tworzenie tabeli
# create_all tworzy tabelę w bazie danych zgodnie z zdefiniowanym modelem
Base.metadata.create_all(engine)

# Dodawanie rekordu do tabeli
# Session to kontekst sesji bazy danych, pozwala na zarządzanie
# rekordami (dodawanie, modyfikowanie, usuwanie)
with Session(engine) as session:
    new_record = ExampleTable(name="Przykład", description="Opis przykładu")  # Tworzenie nowego rekordu
    session.add(new_record)  # Dodawanie rekordu do sesji
    session.commit()  # Zatwierdzenie zmian w bazie danych

# Pobieranie i wyświetlanie rekordów z tabeli
with Session(engine) as session:
    result = session.query(ExampleTable).all()  # Pobieranie wszystkich rekordów z tabeli
    for row in result:
        print(f"ID: {row.id}, Name: {row.name}, Description: {row.description}")