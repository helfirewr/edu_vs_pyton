import psycopg2
from DB import *

# Stworzymy procedurę składowaną z użyciem pętli. Załóżmy, że mamy tabelę documents,
# która zawiera informacje o różnych dokumentach i ich statusach.
# Utworzymy procedurę, która przejdzie przez wszystkie dokumenty
# i zaktualizuje ich status na podstawie określonego kryterium.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'documents'
    cursor.execute("""
        DROP TABLE IF EXISTS documents;
        CREATE TABLE documents (
            document_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            status VARCHAR(50) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'documents'
    cursor.execute("""
        INSERT INTO documents (title, status) 
        VALUES 
            ('Dokument A', 'Pending'),
            ('Dokument B', 'Approved'),
            ('Dokument C', 'Pending');
    """)

    # Tworzenie procedury składowanej z pętlą
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_document_statuses()
        RETURNS VOID AS $$
        DECLARE
            record RECORD;
        BEGIN
            FOR record IN SELECT * FROM documents WHERE status = 'Pending'
            LOOP
                UPDATE documents SET status = 'Reviewed' WHERE document_id = record.document_id;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury
    cursor.callproc('update_document_statuses')

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlenie wszystkich rekordów
    cursor.execute("SELECT * FROM documents")
    documents = cursor.fetchall()

    print("Stan dokumentów po aktualizacji:")
    for doc in documents:
        print(doc)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
