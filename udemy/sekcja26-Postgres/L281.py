import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Dodanie pracownika i zwrócenie jego ID
    insert_query = """
    INSERT INTO employees (first_name, last_name, position, salary)
    VALUES ('Jan', 'Nowak', 'Developer', 5000)
    RETURNING id
    """
    cursor.execute(insert_query)
    new_employee_id = cursor.fetchone()[0]

    print(f"ID nowo dodanego pracownika: {new_employee_id}")

    # Zatwierdzanie zmian
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas dodawania pracownika do bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
