import psycopg2
from DB import *

# Stworzymy przykład procedury, która przyjmuje tablicę identyfikatorów (ID)
# jako parametr i zwraca rekordy pasujące do tych ID. W tym przykładzie utworzymy
# tabelę products z kolumnami id, name i category. Następnie stworzymy procedurę,
# która przyjmuje tablicę ID produktów i zwraca szczegóły tych produktów.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'products'
    cursor.execute("""
        DROP TABLE IF EXISTS products;
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(50) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'products'
    cursor.execute("""
        INSERT INTO products (name, category) 
        VALUES 
            ('Laptop', 'Electronics'),
            ('Książka "Python dla początkujących"', 'Books'),
            ('Smartfon', 'Electronics'),
            ('Kawa', 'Food');
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_products_by_ids(ids INT[])
        RETURNS TABLE(id INT, name VARCHAR, category VARCHAR) AS $$
        BEGIN
            RETURN QUERY SELECT p.id, p.name, p.category FROM products p WHERE p.id = ANY(ids);
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('get_products_by_ids', ([1, 3],))
    products = cursor.fetchall()
    for product in products:
        print(product)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
