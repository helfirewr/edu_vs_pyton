import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Rozszerzenie tabeli 'employees' o dodatkowe kolumny
    alter_table_query = """
        ALTER TABLE employees
        ADD COLUMN email VARCHAR(100) DEFAULT 'unknown@email.com',
        ADD COLUMN salary DECIMAL DEFAULT 0.0
    """
    cursor.execute(alter_table_query)

    # Aktualizacja niektórych rekordów
    update_records_query = """
        UPDATE employees
        SET email = 'anna.kowalska@example.com', salary = 5000.00
        WHERE id = 2
    """
    cursor.execute(update_records_query)

    # Zatwierdzanie zmian
    connection.commit()

    # Wyświetlanie zaktualizowanych danych rekordów
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("Zaktualizowane dane z tabeli 'employees':")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas pracy z bazą danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
