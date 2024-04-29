import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from DB import *
# Dane do połączenia z bazą danych PostgreSQL

database = "postgres"  # Łączymy się z bazą domyślną, aby stworzyć nową bazę danych

try:
    # Nawiązanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)

    # Ustawienie poziomu izolacji na AUTOCOMMIT
    # Pozwala to na natychmiastowe wykonywanie poleceń SQL bez konieczności wywoływania
    # commit().
    # Jest to potrzebne, ponieważ niektóre polecenia, takie jak tworzenie bazy danych,
    # muszą być wykonywane poza transakcją.
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Utworzenie kursora
    cursor = connection.cursor()

    # Tworzenie nowej bazy danych
    cursor.execute("CREATE DATABASE py_test2")

    print("Baza danych py_test2 została pomyślnie utworzona.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas tworzenia bazy danych:", error)
finally:
    # Zawsze zamykaj połączenie i kursor
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")

