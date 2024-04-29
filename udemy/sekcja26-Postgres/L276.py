import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytania SQL z użyciem MIN, MAX, AVG, SUM
    cursor.execute("SELECT MIN(salary) FROM employees")
    min_salary = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(salary) FROM employees")
    max_salary = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(salary) FROM employees")
    avg_salary = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(salary) FROM employees")
    total_salary = cursor.fetchone()[0]

    print(f"Minimalne wynagrodzenie: {min_salary}")
    print(f"Maksymalne wynagrodzenie: {max_salary}")
    print(f"Średnie wynagrodzenie: {avg_salary:.2f}")
    print(f"Suma wszystkich wynagrodzeń: {total_salary}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
