import random
import psycopg2
from DB import *

# W kolejnym przykładzie stworzymy procedurę składowaną, która używa tablicy
# i wybiera losowy element z tabeli. Załóżmy, że mamy tabelę animals, która zawiera
# listę zwierząt. Procedura będzie losowo wybierać nazwę zwierzęcia z tej tabeli
# i zwracać ją jako wynik

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'animals'
    cursor.execute("""
        DROP TABLE IF EXISTS animals;
        CREATE TABLE animals (
            animal_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'animals'
    cursor.execute("""
        INSERT INTO animals (name) 
        VALUES 
            ('Lew'), ('Tygrys'), ('Żyrafa'), ('Słoń');
    """)

    # Tworzenie procedury składowanej wybierającej losowe zwierzę
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_random_animal()
        RETURNS VARCHAR AS $$
        DECLARE
            animals_list VARCHAR[];
            animal_count INTEGER;
            random_index INTEGER;
        BEGIN
            SELECT ARRAY_AGG(name) INTO animals_list FROM animals;
            SELECT COUNT(*) INTO animal_count FROM animals;
            random_index := TRUNC(random() * animal_count) + 1;
            RETURN animals_list[random_index];
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('get_random_animal')
    random_animal = cursor.fetchone()[0]
    print(f"Losowe zwierzę: {random_animal}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
