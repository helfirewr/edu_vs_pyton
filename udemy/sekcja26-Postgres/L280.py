import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem podzapytania
    # W tym przykładzie, użyjemy podzapytania w tabeli employees
    # do znalezienia pracowników, których wynagrodzenie jest wyższe niż średnie
    # wynagrodzenie we wszystkich rekordach.
    subquery_query = """
        SELECT first_name, last_name, salary FROM employees
        WHERE salary > (SELECT AVG(salary) FROM employees)
    """
    cursor.execute(subquery_query)
    records = cursor.fetchall()

    print("Pracownicy z wynagrodzeniem wyższym niż średnia w firmie:")
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
