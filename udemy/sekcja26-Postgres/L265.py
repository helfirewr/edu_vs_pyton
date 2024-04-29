import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie z użyciem IN
    select_query_in = """
    SELECT * FROM employees
    WHERE position IN ('Analyst', 'Developer')
    """
    cursor.execute(select_query_in)
    records = cursor.fetchall()

    print("Pracownicy na stanowiskach 'Analyst' lub 'Developer':")
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
