import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # FULL JOIN łączy funkcjonalności LEFT JOIN i RIGHT JOIN.
    # FULL JOIN zwraca wszystkie rekordy, gdy jest dopasowanie w lewej (LEFT)
    # lub prawej (RIGHT) tabeli. Jeśli nie ma dopasowania, wynikiem dla brakujących
    # stron będzie NULL.

    # Załóżmy, że mamy dwie tabele: clients i orders. Nie każdy klient musi
    # mieć zamówienie i nie każde zamówienie musi być przypisane do klienta.
    # Wykorzystamy FULL JOIN, aby wyświetlić wszystkich klientów i wszystkie
    # zamówienia, niezależnie od tego, czy istnieje między nimi relacja.

    # Tworzenie tabeli 'clients'
    cursor.execute("""
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS clients;
        CREATE TABLE clients (
            client_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'orders'
    cursor.execute("""
        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            order_date DATE NOT NULL,
            client_id INTEGER REFERENCES clients(client_id)
        );
    """)

    # Dodawanie rekordów do tabeli 'clients'
    cursor.execute("""
        INSERT INTO clients (name) 
        VALUES ('Firma A'), ('Firma B');
    """)

    # Dodawanie rekordów do tabeli 'orders'
    cursor.execute("""
        INSERT INTO orders (order_date, client_id) 
        VALUES ('2023-01-01', 1), ('2023-01-02', NULL);
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomocą FULL JOIN
    cursor.execute("""
        SELECT c.name, o.order_date
        FROM clients c
        FULL JOIN orders o ON c.client_id = o.client_id
    """)
    records = cursor.fetchall()

    print("Klienci i ich zamówienia:")
    for row in records:
        print(f"Klient: {row[0]}, Data zamówienia: {row[1]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
