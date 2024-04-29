# pip install psycopg2
# pip uninstall psycopg2
import psycopg2

# Dane do połączenia z bazą danych PostgreSQL
host = "localhost"
user = "postgres"
password = "postgres"
database = "postgres"
connection=None
cursor=None
# Nawiązywanie połączenia z bazą danych
try:
    # Utworzenie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)

    # Utworzenie kursora, który umożliwia wykonywanie operacji na bazie danych
    cursor = connection.cursor()

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if (connection):
        print("Połączenie z bazą działa.")

        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
