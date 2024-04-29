import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()
    connection.autocommit=False
    cursor=connection.cursor()

    cursor.execute("""
        CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER)
        RETURNS INTEGER AS $$
        BEGIN
            RETURN a+b;
        END;
        $$ LANGUAGE plpgsql
    """)

    cursor.callproc('add_numbers', (10,20))
    sum=cursor.fetchone()[0]
    print(f"Wynik dodawania: {sum}")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
