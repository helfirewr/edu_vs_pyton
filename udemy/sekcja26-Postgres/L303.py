import psycopg2
from DB import *

# Stworzymy przykład procedury w PostgreSQL, która używa pętli FOREACH do iteracji
# po elementach tablicy. W tym przykładzie utworzymy tabelę tasks z kolumnami id,
# name i status. Następnie stworzymy procedurę, która przyjmuje tablicę identyfikatorów
# zadań i aktualizuje ich status.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # Tworzenie tabeli 'tasks'
    cursor.execute("""
        DROP TABLE IF EXISTS tasks;
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'Pending'
        );
    """)

    # Dodawanie danych do tabeli 'tasks'
    cursor.execute("""
        INSERT INTO tasks (name) 
        VALUES 
            ('Task 1'),
            ('Task 2'),
            ('Task 3'),
            ('Task 4');
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_task_status(task_ids INT[], new_status VARCHAR)
        RETURNS VOID AS $$
        DECLARE
            task_id INT;
        BEGIN
            FOREACH task_id IN ARRAY task_ids
            LOOP
                UPDATE tasks SET status = new_status WHERE id = task_id;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlenie wyniku
    cursor.callproc('update_task_status', ([1, 3], 'Completed'))
    connection.commit()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
