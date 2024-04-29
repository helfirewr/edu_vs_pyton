import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem BETWEEN AND
    select_query_between = """
        SELECT * FROM employees
        WHERE salary BETWEEN 4000 AND 6000
    """
    cursor.execute(select_query_between)
    records = cursor.fetchall()

    print("Pracownicy z wynagrodzeniem pomiędzy 4000 a 6000:")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
