import psycopg2
from DB import *

try:
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Zapytanie SQL do utworzenia nowej tabeli
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        birth_date DATE,
        position VARCHAR(50)
    )
    '''
    cursor.execute(create_table_query)

    # Zatwierdzanie zmian w bazie danych
    connection.commit()

    print("Tabela 'employees' została pomyślnie utworzona.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas tworzenia tabeli:", error)
finally:
    # Zawsze zamykaj połączenie i kursor
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
