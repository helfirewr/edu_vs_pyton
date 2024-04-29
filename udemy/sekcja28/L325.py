import unittest
import psycopg2
from psycopg2 import sql

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Nawiązanie połączenia z bazą danych
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="py_todo"
        )
        self.cur = self.conn.cursor()

        # Usunięcie tabeli jeśli istnieje
        self.cur.execute("DROP TABLE IF EXISTS test_table;")
        self.conn.commit()

        # Utworzenie nowej tabeli
        self.cur.execute("""
            CREATE TABLE test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                value INTEGER
            );
        """)
        self.conn.commit()

    def test_insert_and_select(self):
        # Wstawienie danych do tabeli
        self.cur.execute("INSERT INTO test_table (name, value) VALUES (%s, %s);", ("test", 123))
        self.conn.commit()

        # Pobranie i sprawdzenie wstawionych danych
        self.cur.execute("SELECT * FROM test_table WHERE name = %s;", ("test",))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "test")
        self.assertEqual(result[2], 123)

    def test_update_and_delete(self):
        # Wstawienie danych do tabeli
        self.cur.execute("INSERT INTO test_table (name, value) VALUES (%s, %s);", ("update_test", 456))
        self.conn.commit()

        # Aktualizacja danych
        self.cur.execute("UPDATE test_table SET value = %s WHERE name = %s;", (789, "update_test"))
        self.conn.commit()

        # Sprawdzenie aktualizacji
        self.cur.execute("SELECT * FROM test_table WHERE name = %s;", ("update_test",))
        result = self.cur.fetchone()
        self.assertEqual(result[2], 789)

        # Usunięcie danych
        self.cur.execute("DELETE FROM test_table WHERE name = %s;", ("update_test",))
        self.conn.commit()

        # Sprawdzenie usunięcia
        self.cur.execute("SELECT * FROM test_table WHERE name = %s;", ("update_test",))
        result = self.cur.fetchone()
        self.assertIsNone(result)

    def tearDown(self):
        # Zamknięcie połączenia z bazą danych
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
