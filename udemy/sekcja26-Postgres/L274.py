import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Modyfikacja kolumny 'salary' na typ INTEGER
    alter_column_query = "ALTER TABLE employees ALTER COLUMN salary TYPE INTEGER"
    cursor.execute(alter_column_query)

    # Pobieranie danych po modyfikacji
    cursor.execute("SELECT id, first_name, salary FROM employees")
    records = cursor.fetchall()

    print("Dane z tabeli 'employees' po zmianie typu kolumny 'salary':")
    for row in records:
        print(row)

    # Zatwierdzanie zmian
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas modyfikacji tabeli lub odczytywania z bazy danych:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
