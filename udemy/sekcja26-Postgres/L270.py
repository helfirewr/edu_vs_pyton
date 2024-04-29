import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie z użyciem LIMIT i OFFSET
    print("3 rekordy z tabeli 'employees', zaczynając od trzeciego rekordu:")
    cursor.execute("SELECT * FROM employees LIMIT 3 OFFSET 3")
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
