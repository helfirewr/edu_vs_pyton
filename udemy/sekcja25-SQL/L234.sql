CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER)
RETURNS INTEGER AS $$
BEGIN
	RETURN a + b;
END;
$$ LANGUAGE plpgsql;

/*
CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER):
  Ta linia tworzy nową funkcję o nazwie add_numbers, która przyjmuje dwa
  argumenty: a i b, oba typu INTEGER. Słowo kluczowe CREATE OR REPLACE oznacza,
  że jeśli funkcja o tej nazwie już istnieje, zostanie zastąpiona nową definicją.

RETURNS INTEGER AS $$  Ta linia definiuje typ danych, który zostanie zwrócony
  przez funkcję. W tym przypadku funkcja zwraca wartość typu INTEGER. AS $$
  rozpoczyna blok definicji funkcji.

BEGIN  Słowo kluczowe BEGIN rozpoczyna blok kodu funkcji.

RETURN a + b;  Ta linia jest ciałem funkcji. Wykonuje operację dodawania na
  argumentach a i b, a następnie zwraca wynik.

END;  Słowo kluczowe END kończy blok kodu funkcji.

$$ LANGUAGE plpgsql;  Ta linia kończy definicję funkcji. $$ kończy blok
   definicji funkcji. LANGUAGE plpgsql określa, że funkcja jest napisana w
   języku plpgsql, który jest proceduralnym językiem PostgreSQL.

*/

SELECT add_numbers(4, 3);