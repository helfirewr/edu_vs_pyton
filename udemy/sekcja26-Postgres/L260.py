import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Identyfikator rekordu do usunięcia
    id_to_delete = 1

    # Zapytanie SQL do usunięcia rekordu z tabeli 'employees'
    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (id_to_delete,))

    # Zatwierdzanie zmian
    connection.commit()

    print(f"Rekord o ID {id_to_delete} został usunięty z tabeli 'employees'.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas usuwania rekordu z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
