import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie z użyciem NOT
    select_query_not = """
        SELECT * FROM employees
        WHERE first_name NOT LIKE 'Imie%'
    """
    cursor.execute(select_query_not)
    records = cursor.fetchall()

    print("Pracownicy, których imię nie zaczyna się od 'Imie':")
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
