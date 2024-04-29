import psycopg2
from DB import *

# Stworzymy procedurę, która łączy dane za pomocą funkcji CONCAT.
# Załóżmy, że mamy tabelę cities, która zawiera informacje o różnych miastach,
# ich krajach i populacji. Utworzymy procedurę, która zwraca sformatowany
# ciąg tekstowy dla każdego miasta, łącząc jego nazwę, kraj i populację.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'cities'
    cursor.execute("""
        DROP TABLE IF EXISTS cities;
        CREATE TABLE cities (
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL,
            population INTEGER
        );
    """)

    # Dodawanie danych do tabeli 'cities'
    cursor.execute("""
        INSERT INTO cities (name, country, population) 
        VALUES 
            ('Warszawa', 'Polska', 1700000),
            ('Kraków', 'Polska', 760000),
            ('Berlin', 'Niemcy', 3600000);
    """)

    # Tworzenie procedury składowanej zwracającej sformatowane informacje o miastach
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_city_details()
        RETURNS TABLE(details TEXT)
        AS $$
        BEGIN
            RETURN QUERY SELECT CONCAT(name, ', ', country, ' - Populacja: ', population)
            FROM cities;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('get_city_details')
    city_details = cursor.fetchall()
    print("Informacje o miastach:")
    for detail in city_details:
        print(detail[0])

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
