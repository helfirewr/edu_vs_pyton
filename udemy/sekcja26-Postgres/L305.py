import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'printers'
    cursor.execute("""
        DROP TABLE IF EXISTS printers;
        CREATE TABLE printers (
            id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'Idle'
        );
    """)

    # Dodawanie danych do tabeli 'printers'
    cursor.execute("""
        INSERT INTO printers (model, status) 
        VALUES 
            ('Printer A', 'Idle'),
            ('Printer B', 'Printing'),
            ('Printer C', 'Idle');
    """)

    # Tworzenie procedury składowanej
    # exit wyjdzie z pętli jeśli drukarka drukuje
    cursor.execute("""
        CREATE OR REPLACE FUNCTION check_printing_status()
        RETURNS VARCHAR AS $$
        DECLARE
            printer RECORD;
        BEGIN
            FOR printer IN SELECT * FROM printers
            LOOP
                IF printer.status = 'Printing' THEN
                    RETURN printer.model || ' is currently printing.';
                    EXIT;
                END IF;
            END LOOP;
            RETURN 'All printers are idle.';
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('check_printing_status')
    result = cursor.fetchone()[0]
    print(result)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
