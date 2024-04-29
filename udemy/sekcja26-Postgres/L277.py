import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem GROUP BY
    # użyjemy GROUP BY do zgrupowania pracowników z tabeli employees według ich stanowiska
    group_by_query = """
        SELECT position, AVG(salary) AS average_salary
        FROM employees
        GROUP BY position
    """
    cursor.execute(group_by_query)
    records = cursor.fetchall()

    print("Średnie wynagrodzenie dla każdego stanowiska:")
    for row in records:
        print(f"Stanowisko: {row[0]}, Średnie wynagrodzenie: {row[1]:.2f}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
