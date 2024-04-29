import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'departments'
    cursor.execute("""
        DROP TABLE IF EXISTS departments;
        CREATE TABLE departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'employees'
    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        CREATE TABLE employees (
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            department_id INTEGER REFERENCES departments(department_id)
        );
    """)

    # Dodawanie rekordów do tabeli 'departments'
    cursor.execute("""
        INSERT INTO departments (department_name) 
        VALUES ('HR'), ('IT'), ('Finance');
    """)

    # Dodawanie rekordów do tabeli 'employees'
    cursor.execute("""
        INSERT INTO employees (first_name, last_name, department_id) 
        VALUES ('Jan', 'Kowalski', 1), ('Anna', 'Nowak', 2), ('Piotr', 'Wiśniewski', 2);
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów z obu tabel za pomocą JOIN
    cursor.execute("""
        SELECT e.first_name, e.last_name, d.department_name
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
    """)
    records = cursor.fetchall()

    print("Pracownicy i ich działy:")
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
