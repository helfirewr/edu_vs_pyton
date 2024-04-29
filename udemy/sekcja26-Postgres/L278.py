import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # W tym przykładzie, zgrupujemy pracowników z tabeli employees według
    # ich stanowiska (position) i obliczymy średnie wynagrodzenie dla każdego stanowiska,
    # ale za pomocą HAVING wybierzemy tylko te stanowiska, na których średnie wynagrodzenie
    # przekracza określoną wartość.
    group_by_having_query = """
        SELECT position, AVG(salary) AS average_salary
        FROM employees
        GROUP BY position
        HAVING AVG(salary) > 5000
    """
    cursor.execute(group_by_having_query)
    records = cursor.fetchall()

    print("Stanowiska ze średnim wynagrodzeniem powyżej 5000:")
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
