import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from DB import *

# Stworzymy teraz prosty przykład wykorzystujący TRIGGER w PostgreSQL,
# który będzie aktualizował dane rekordu przy zapisie, odnosząc się do tematu monitorów.
# Utworzymy tabelę monitors z kolumnami id, model, price i last_updated.
# Następnie zdefiniujemy TRIGGER, który zaktualizuje kolumnę last_updated
# do bieżącej daty i godziny przy każdej aktualizacji rekordu w tabeli monitors.

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Tworzenie tabeli 'monitors'
    cursor.execute("""
        DROP TABLE IF EXISTS monitors;
        CREATE TABLE monitors (
            id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Dodawanie danych do tabeli 'monitors'
    cursor.execute("""
        INSERT INTO monitors (model, price) 
        VALUES 
            ('Monitor A', 200.00),
            ('Monitor B', 250.00);
    """)

    # Tworzenie funkcji wyzwalającej 'trigger'
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_last_updated()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.last_updated = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Utworzenie 'TRIGGER'
    cursor.execute("""
        CREATE TRIGGER update_monitor_last_updated
        BEFORE UPDATE ON monitors
        FOR EACH ROW
        EXECUTE FUNCTION update_last_updated();
    """)

    # Aktualizacja rekordu, aby wyzwolić 'TRIGGER'
    cursor.execute("""
        UPDATE monitors SET price = 210.00 WHERE model = 'Monitor A';
    """)

    # Wyświetlenie zaktualizowanych danych
    cursor.execute("SELECT * FROM monitors")
    monitors = cursor.fetchall()
    for monitor in monitors:
        print(monitor)

except (Exception, psycopg2.DatabaseError) as error:
    print("Wystąpił błąd:", error)
finally:
    # Zamykanie połączenia
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
