import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # CROSS JOIN w SQL jest używany do tworzenia kombinacji kartezjańskiej dwóch tabel,
    # co oznacza, że każdy wiersz z pierwszej tabeli jest łączony z każdym wierszem
    # z drugiej tabeli. W rezultacie liczba wierszy w wynikowym zbiorze danych
    # jest równa iloczynowi liczby wierszy w obu tabelach.

    # Załóżmy, że mamy dwie tabele: colors i shapes, i chcemy stworzyć wszystkie
    # możliwe kombinacje kolorów i kształtów.

    # Tworzenie tabeli 'colors'
    cursor.execute("""
        DROP TABLE IF EXISTS shapes;
        DROP TABLE IF EXISTS colors;
        CREATE TABLE colors (
            color_id SERIAL PRIMARY KEY,
            color_name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'shapes'
    cursor.execute("""
        CREATE TABLE shapes (
            shape_id SERIAL PRIMARY KEY,
            shape_name VARCHAR(255) NOT NULL
        );
    """)

    # Dodawanie rekordów do tabeli 'colors'
    cursor.execute("""
        INSERT INTO colors (color_name) 
        VALUES ('Red'), ('Green'), ('Blue');
    """)

    # Dodawanie rekordów do tabeli 'shapes'
    cursor.execute("""
        INSERT INTO shapes (shape_name) 
        VALUES ('Circle'), ('Square'), ('Triangle');
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomocą CROSS JOIN
    cursor.execute("""
        SELECT c.color_name, s.shape_name
        FROM colors c
        CROSS JOIN shapes s
    """)
    records = cursor.fetchall()

    print("Wszystkie kombinacje kolorów i kształtów:")
    for row in records:
        print(f"Kolor: {row[0]}, Kształt: {row[1]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
