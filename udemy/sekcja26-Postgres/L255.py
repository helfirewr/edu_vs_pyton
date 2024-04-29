import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from DB import *
# Dane do połączenia z bazą danych PostgreSQL
# Łączymy się z bazą domyślną, aby usunąć inną bazę danych

try:
    # Nawiązanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)

    # Ustawienie poziomu izolacji na AUTOCOMMIT
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Utworzenie kursora
    cursor = connection.cursor()

    # Usuwanie bazy danych
    cursor.execute("DROP DATABASE IF EXISTS py_test2")

    print("Baza danych py_test2 została pomyślnie usunięta.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas usuwania bazy danych:", error)
finally:
    # Zawsze zamykaj połączenie i kursor
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")

