import psycopg2
from DB import *

# Utworzymy tabelę vegetables z kolumnami id, name i quantity.
# Następnie stworzymy procedurę, która iteruje przez warzywa w tabeli i,
# jeśli ilość danego warzywa jest poniżej określonego progu, procedura użyje
# instrukcji CONTINUE do pominięcia aktualizacji ceny tego warzywa.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'vegetables'
    cursor.execute("""
        DROP TABLE IF EXISTS vegetables;
        CREATE TABLE vegetables (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL DEFAULT 0.00
        );
    """)

    # Dodawanie danych do tabeli 'vegetables'
    cursor.execute("""
        INSERT INTO vegetables (name, quantity, price) 
        VALUES 
            ('Tomato', 100, 0.50),
            ('Cucumber', 30, 0.30),
            ('Carrot', 50, 0.20),
            ('Lettuce', 10, 0.40);
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_vegetable_prices(min_quantity INT, price_increase DECIMAL)
        RETURNS VOID AS $$
        DECLARE
            vegetable RECORD;
        BEGIN
            FOR vegetable IN SELECT * FROM vegetables
            LOOP
                IF vegetable.quantity < min_quantity THEN
                    CONTINUE;
                END IF;
                UPDATE vegetables SET price = price + price_increase WHERE id = vegetable.id;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('update_vegetable_prices', (20, 0.05))
    connection.commit()

    cursor.execute("SELECT * FROM vegetables")
    vegetables = cursor.fetchall()
    for vegetable in vegetables:
        print(vegetable)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
