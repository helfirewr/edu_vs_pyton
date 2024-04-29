import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Usuwanie i tworzenie tabeli 'game_studios'
    cursor.execute("""
        DROP TABLE IF EXISTS employees CASCADE;
        DROP TABLE IF EXISTS game_studios CASCADE;
        CREATE TABLE game_studios (
            studio_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'employees'
    cursor.execute("""
        CREATE TABLE employees (
            employee_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            position VARCHAR(50) NOT NULL,
            studio_id INT NOT NULL,
            FOREIGN KEY (studio_id) REFERENCES game_studios(studio_id)
        );
    """)

    # Dodawanie danych do tabeli 'game_studios'
    cursor.execute("""
        INSERT INTO game_studios (name) VALUES ('CD Projekt Red'), ('Ubisoft'), ('Valve');
    """)

    # Dodawanie danych do tabeli 'employees'
    cursor.execute("""
        INSERT INTO employees (name, position, studio_id) VALUES 
            ('Jan Kowalski', 'Developer', 1),
            ('Anna Nowak', 'Artist', 1),
            ('Tomasz Wiśniewski', 'Designer', 2);
    """)

    # Aktualizowanie rekordu w 'employees'
    cursor.execute("""
        UPDATE employees SET position = 'Senior Developer' WHERE name = 'Jan Kowalski';
    """)

    # Usuwanie rekordu z 'employees'
    cursor.execute("""
        DELETE FROM employees WHERE name = 'Anna Nowak';
    """)

    # Odczytywanie danych z 'employees'
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    print("Pracownicy:")
    for employee in employees:
        print(employee)

    # JOIN między 'game_studios' i 'employees'
    cursor.execute("""
        SELECT game_studios.name, employees.name, employees.position
        FROM game_studios
        JOIN employees ON game_studios.studio_id = employees.studio_id;
    """)
    joined_data = cursor.fetchall()
    print("\nPracownicy i ich studia:")
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
