import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie typu ENUM
    cursor.execute("""
        DROP TYPE IF EXISTS project_status;
        CREATE TYPE project_status AS ENUM ('Active', 'Pending', 'Completed');
    """)

    # Tworzenie tabeli 'projects'
    cursor.execute("""
        DROP TABLE IF EXISTS projects;
        CREATE TABLE projects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            status project_status
        );
    """)

    # Dodawanie rekordów do tabeli 'projects'
    cursor.execute("""
        INSERT INTO projects (name, status) 
        VALUES ('Project A', 'Active');
    """)
    cursor.execute("""
        INSERT INTO projects (name, status) 
        VALUES ('Project B', 'Pending');
    """)
    cursor.execute("""
        INSERT INTO projects (name, status) 
        VALUES ('Project C', 'Completed');
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów
    cursor.execute("SELECT * FROM projects")
    records = cursor.fetchall()

    print("Rekordy w tabeli 'projects':")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
