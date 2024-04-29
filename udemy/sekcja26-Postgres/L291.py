import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()
    cursor=connection.cursor()
    cursor = connection.cursor()
    cursor.execute("""
            DROP TABLE IF EXISTS employees;
            CREATE TABLE employees(
                employee_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL
            );
            INSERT INTO employees (first_name, last_name)
            VALUES 
                ('Tomasz', 'Nowak'),
                ('Adam','Kowal'),
                ('Anna','Leń'),
                ('Magda','Bizoń');
        """)
    cursor.execute("""
        CREATE OR REPLACE FUNCTION count_employees()
        RETURNS INTEGER AS $$
        DECLARE 
            emp_count INTEGER;
        BEGIN
            SELECT COUNT(*) INTO emp_count from employees;
            RETURN emp_count;
        END;
        $$ LANGUAGE plpgsql
    """)

    cursor.callproc('count_employees')
    sum=cursor.fetchone()[0]
    print(f"Ilość pracowników: {sum}")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")