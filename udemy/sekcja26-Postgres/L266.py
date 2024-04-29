import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie z użyciem LIKE dla "Imie8"
    select_query_like = """
        SELECT * FROM employees
        WHERE first_name LIKE 'Imie_8%'
    """
    cursor.execute(select_query_like)
    records = cursor.fetchall()

    print("Pracownicy, których imię zaczyna się od 'Imie8':")
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
