import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()
    connection.autocommit=False
    cursor=connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        DROP TABLE IF EXISTS departments;
        CREATE TABLE departments(
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(255) NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE employees(
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            department_id INTEGER REFERENCES departments(department_id)
        );
    """)

    cursor.execute("""
        INSERT INTO departments(department_name)
        VALUES 
            ('HR'),('DEV'),('Marketing');
    """)

    cursor.execute("""
        INSERT INTO employees (first_name, last_name, department_id)
        VALUES 
            ('Tomasz', 'Nowak',2),
            ('Adam','Kowal',2),
            ('Anna','Leń',1),
            ('Magda','Bizoń',3);
    """)

    cursor.execute("""
        UPDATE departments set department_name = 'IT' where department_id=2;
    """)

    connection.commit()
    print("Transakcja zakończona pozytywnie")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
