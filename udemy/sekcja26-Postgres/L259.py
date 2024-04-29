import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL do odczytu danych z tabeli 'employees'
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)

    # Pobieranie wyników zapytania
    records = cursor.fetchall()

    print("Dane z tabeli 'employees':")
    for row in records:
        print(f"ID: {row[0]}, Imię: {row[1]}, Nazwisko: {row[2]}, Stanowisko: {row[4]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
