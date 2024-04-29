import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem AS do nadania aliasów
    cursor.execute("SELECT first_name AS \"First Name\", last_name AS \"Last Name\" FROM employees")
    records = cursor.fetchall()

    print("Imiona i nazwiska pracowników:")
    for row in records:
        first_name, last_name = row
        print(f"First Name: {first_name}, Last Name: {last_name}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
