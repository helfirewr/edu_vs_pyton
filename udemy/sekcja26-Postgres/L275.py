import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem COUNT
    count_query = "SELECT COUNT(*) FROM employees"
    cursor.execute(count_query)

    # Pobieranie wyniku
    count_result = cursor.fetchone()
    total_employees = count_result[0]

    print(f"Łączna liczba pracowników: {total_employees}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
