import psycopg2
from DB import *

# W kolejnym przykładzie stworzymy procedurę składowaną z parametrem wyjściowym OUT,
# który pozwoli zwrócić dane z procedury. Załóżmy, że mamy tabelę products
# i chcemy utworzyć procedurę, która zwraca ilość produktów danego typu.

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
            category VARCHAR(50) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'products'
    cursor.execute("""
        INSERT INTO products (name, category, price) 
        VALUES 
            ('Laptop', 'Electronics', 3000.00),
            ('Smartphone', 'Electronics', 2000.00),
            ('Book "Learn SQL"', 'Books', 100.00),
            ('Coffee', 'Food', 20.00);
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION count_products_by_category(category_name VARCHAR)
        RETURNS INTEGER AS $$
        DECLARE
            product_count INTEGER;
        BEGIN
            SELECT COUNT(*) INTO product_count FROM products WHERE category = category_name;
            RETURN product_count;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('count_products_by_category', ('Electronics',))
    count = cursor.fetchone()[0]
    print(f"Ilość produktów w kategorii 'Electronics': {count}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
