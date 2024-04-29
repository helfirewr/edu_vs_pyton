import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem ORDER BY do sortowania danych
    select_query = "SELECT id, first_name, last_name, salary FROM employees ORDER BY id DESC"
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("Dane z tabeli 'employees' posortowane według wynagrodzenia (malejąco):")
    for row in records:
        print(f"ID: {row[0]}, Imię: {row[1]}, Nazwisko: {row[2]}, Wynagrodzenie: {row[3]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
