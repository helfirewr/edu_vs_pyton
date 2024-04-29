import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem DISTINCT do wyświetlenia unikalnych wartości salary
    select_query = "SELECT DISTINCT salary FROM employees"
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("Unikalne wartości w tabeli 'employees':")
    for row in records:
        print(f"salary: {row[0]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
