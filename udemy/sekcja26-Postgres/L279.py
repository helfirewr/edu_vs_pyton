import psycopg2
from DB import *
try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem UNION ALL
    # W tym przykładzie, wykorzystamy UNION ALL do połączenia dwóch zapytań
    # z tabeli employees: jedno zapytanie wybierze pracowników na stanowisku 'Manager',
    # a drugie pracowników na stanowisku 'Developer'.
    union_all_query = """
    SELECT first_name, last_name, position FROM employees WHERE position = 'Manager'
    UNION ALL
    SELECT first_name, last_name, position FROM employees WHERE position = 'Developer'
    """
    cursor.execute(union_all_query)
    records = cursor.fetchall()

    print("Pracownicy na stanowiskach 'Manager' i 'Developer':")
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
