import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie z użyciem LIMIT
    print("Pierwsze 3 rekordy z tabeli 'employees':")
    cursor.execute("SELECT * FROM employees LIMIT 3")
    for row in cursor.fetchall():
        print(row)

    # Zapytanie z użyciem LIMIT i AND
    print("\nMaksymalnie 2 rekordy menedżerów z wynagrodzeniem powyżej 4000:")
    cursor.execute("SELECT * FROM employees WHERE salary > 4000 LIMIT 2")
    for row in cursor.fetchall():
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
