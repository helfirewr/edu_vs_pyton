import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Tworzenie tabeli 'manufacturers'
    cursor.execute("""
        DROP TABLE IF EXISTS manufacturers;
        CREATE TABLE manufacturers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'laptops'
    cursor.execute("""
        DROP TABLE IF EXISTS laptops;
        CREATE TABLE laptops (
            id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            manufacturer_id INT NOT NULL,
            price DECIMAL(10, 2),
            FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id)
        );
    """)

    # Dodawanie danych do tabeli 'manufacturers'
    cursor.execute("""
        INSERT INTO manufacturers (name) VALUES ('Lenovo'), ('HP'), ('Dell');
    """)

    # Dodawanie danych do tabeli 'laptops'
    cursor.execute("""
        INSERT INTO laptops (model, manufacturer_id, price) VALUES 
            ('ThinkPad X1', 1, 1200.00),
            ('Pavilion 15', 2, 800.00),
            ('XPS 15', 3, 1600.00);
    """)

    # Aktualizowanie rekordu w 'laptops'
    cursor.execute("""
        UPDATE laptops SET price = 1300.00 WHERE model = 'ThinkPad X1';
    """)

    # Usuwanie rekordu z 'laptops'
    cursor.execute("""
        DELETE FROM laptops WHERE model = 'XPS 15';
    """)

    # Odczytywanie danych z 'laptops'
    cursor.execute("SELECT * FROM laptops")
    laptops = cursor.fetchall()
    print("Laptopy:")
    for laptop in laptops:
        print(laptop)

    # JOIN między 'manufacturers' i 'laptops'
    cursor.execute("""
        SELECT manufacturers.name, laptops.model, laptops.price
        FROM manufacturers
        JOIN laptops ON manufacturers.id = laptops.manufacturer_id;
    """)
    joined_data = cursor.fetchall()
    print("\nLaptopy z producentami:")
    for item in joined_data:
        print(item)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
