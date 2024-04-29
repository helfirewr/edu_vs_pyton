import psycopg2
from DB import *

# Stworzymy teraz przykład z procedurą składowaną, która wykorzystuje
# instrukcję warunkową IF oraz lokalną zmienną. Załóżmy, że mamy tabelę countries
# zawierającą informacje o krajach i ich populacji. Utworzymy procedurę,
# która określi, czy kraj jest "duży", "średni" czy "mały" na podstawie
# jego populacji, i zwróci odpowiednią klasyfikację.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'countries'
    cursor.execute("""
        DROP TABLE IF EXISTS countries;
        CREATE TABLE countries (
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            population INTEGER NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'countries'
    cursor.execute("""
        INSERT INTO countries (name, population) 
        VALUES 
            ('Polska', 38000000),
            ('Monako', 38000),
            ('Niemcy', 83000000);
    """)

    # Tworzenie procedury składowanej z instrukcją warunkową IF
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_country_size(country_name VARCHAR)
        RETURNS TEXT AS $$
        DECLARE
            country_population INTEGER;
            size TEXT;
        BEGIN
            SELECT population INTO country_population FROM countries WHERE name = country_name;
            IF country_population > 50000000 THEN
                size := 'duży';
            ELSIF country_population > 20000000 THEN
                size := 'średni';
            ELSE
                size := 'mały';
            END IF;
            RETURN size;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('get_country_size', ('Polska',))
    size = cursor.fetchone()[0]
    print(f"Rozmiar Polski: {size}")

    cursor.callproc('get_country_size', ('Monako',))
    size = cursor.fetchone()[0]
    print(f"Rozmiar Monako: {size}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
