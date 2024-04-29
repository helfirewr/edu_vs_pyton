import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Dodawanie pojedynczego rekordu do tabeli 'employees'
    insert_query_single = """
        INSERT INTO employees (first_name, last_name, birth_date, position) 
        VALUES ('Jan', 'Kowalski', '1980-01-01', 'Manager')
    """
    cursor.execute(insert_query_single)

    # Dodawanie wielu rekordów za jednym razem
    employees_to_insert = [
        ('Anna', 'Nowak', '1990-05-05', 'Developer'),
        ('Piotr', 'Wiśniewski', '1985-07-09', 'Analyst'),
        ('Ewa', 'Maj', '1992-03-15', 'Designer')
    ]

    insert_query_multiple = """
        INSERT INTO employees (first_name, last_name, birth_date, position) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query_multiple, employees_to_insert)

    # Zatwierdzanie zmian
    connection.commit()

    print("Rekordy zostały dodane do tabeli 'employees'.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas dodawania rekordów do tabeli:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
