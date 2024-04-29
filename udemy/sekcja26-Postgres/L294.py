import psycopg2
from DB import *

# Stworzymy przykład związany z samochodami. Załóżmy, że mamy tabelę cars reprezentującą
# samochody oraz tabelę owners, reprezentującą właścicieli. Następnie stworzymy procedurę,
# która zwraca informacje o samochodach posiadanych przez konkretnego właściciela.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'owners'
    cursor.execute("""
        DROP TABLE IF EXISTS cars;
        DROP TABLE IF EXISTS owners;
        CREATE TABLE owners (
            owner_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'cars'
    cursor.execute("""
        CREATE TABLE cars (
            car_id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            owner_id INTEGER REFERENCES owners(owner_id)
        );
    """)

    # Dodawanie danych do tabeli 'owners'
    cursor.execute("""
        INSERT INTO owners (name) VALUES ('Jan Kowalski'), ('Adam Nowak');
    """)

    # Dodawanie danych do tabeli 'cars'
    cursor.execute("""
        INSERT INTO cars (model, year, owner_id) 
        VALUES 
            ('Toyota Corolla', 2020, 1),
            ('Honda Civic', 2018, 2),
            ('Ford Focus', 2019, 1);
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_cars_by_owner(owner_name VARCHAR)
        RETURNS TABLE(car_id INTEGER, model VARCHAR, year INTEGER)
        AS $$
        BEGIN
            RETURN QUERY 
            SELECT c.car_id, c.model, c.year 
            FROM cars c
            JOIN owners o ON c.owner_id = o.owner_id
            WHERE o.name = owner_name;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('get_cars_by_owner', ('Jan Kowalski',))
    cars = cursor.fetchall()
    print(f"Samochody należące do Jana Kowalskiego:")
    for car in cars:
        print(car)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
