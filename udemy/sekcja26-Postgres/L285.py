import psycopg2
from DB import *

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=database)
    cursor = connection.cursor()

    # LEFT JOIN wybiera wszystkie rekordy z lewej tabeli
    # (tabela po lewej stronie JOIN) i dopasowane rekordy z prawej tabeli
    # (tabela po prawej stronie JOIN). Jeśli nie ma dopasowania, wynikiem dla
    # prawej tabeli będzie NULL.

    # Stworzymy dwie nowe tabele: students i grades, gdzie każdy student może mieć ocenę.
    # Nie wszyscy studenci muszą mieć ocenę, co sprawia, że LEFT JOIN będzie odpowiedni
    # do wyświetlenia wszystkich studentów wraz z ich ocenami, jeśli takie istnieją

    # Tworzenie tabeli 'students'
    cursor.execute("""
        DROP TABLE IF EXISTS grades;
        DROP TABLE IF EXISTS students;
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'grades'
    cursor.execute("""
        CREATE TABLE grades (
            grade_id SERIAL PRIMARY KEY,
            grade VARCHAR(10),
            student_id INTEGER REFERENCES students(student_id)
        );
    """)

    # Dodawanie rekordów do tabeli 'students'
    cursor.execute("""
        INSERT INTO students (name) 
        VALUES ('Jan Kowalski'), ('Anna Nowak');
    """)

    # Dodawanie rekordów do tabeli 'grades'
    cursor.execute("""
        INSERT INTO grades (grade, student_id) 
        VALUES ('A', 1);
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomocą LEFT JOIN
    cursor.execute("""
        SELECT s.name, g.grade
        FROM students s
        LEFT JOIN grades g ON s.student_id = g.student_id
    """)
    records = cursor.fetchall()

    print("Studenci i ich oceny:")
    for row in records:
        print(f"Student: {row[0]}, Ocena: {row[1]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd:", error)
finally:
    # Zamykanie połączenia i kursora
    if connection:
        cursor.close()
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")
