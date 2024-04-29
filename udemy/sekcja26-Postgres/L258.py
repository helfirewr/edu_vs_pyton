import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Aktualizacja wszystkich rekordów
    update_query_all = """
        UPDATE employees
        SET position = 'Senior Manager'
    """
    cursor.execute(update_query_all)

    # Aktualizacja jednego wybranego rekordu, np. o id = 1
    update_query_single = """
        UPDATE employees
        SET position = 'Lead Developer'
        WHERE id = 1
    """
    cursor.execute(update_query_single)

    # Zatwierdzanie zmian
    connection.commit()

    print("Rekordy zostały zaktualizowane w tabeli 'employees'.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas aktualizacji rekordów:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
