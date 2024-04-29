import psycopg2
from DB import *

# W tym przykładzie stworzymy tabelę employees z kolumnami id, name, department i salary.
# Następnie napiszemy procedurę, która aktualizuje wynagrodzenia pracowników w zależności
# od ich działu.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'employees'
    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        CREATE TABLE employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department VARCHAR(50) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'employees'
    cursor.execute("""
        INSERT INTO employees (name, department, salary) 
        VALUES 
            ('Jan Kowalski', 'IT', 5000.00),
            ('Anna Nowak', 'HR', 4500.00),
            ('Piotr Zalewski', 'Marketing', 4000.00);
    """)

    # Tworzenie procedury składowanej z instrukcją CASE
    # która zwróc wartośc aktualizującą wynagrodzenie ze względu
    # na stanowisko
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_employee_salaries()
        RETURNS VOID AS $$
        BEGIN
            UPDATE employees
            SET salary = salary * CASE
                WHEN department = 'IT' THEN 1.10
                WHEN department = 'HR' THEN 1.05
                ELSE 1.03
            END;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury
    cursor.callproc('update_employee_salaries')

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlenie wszystkich rekordów
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("Stan pracowników po aktualizacji wynagrodzeń:")
    for emp in employees:
        print(emp)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
