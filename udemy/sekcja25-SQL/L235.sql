CREATE OR REPLACE FUNCTION multiply_numbers(a INTEGER = 1, b INTEGER = 2)
RETURNS INTEGER AS $$
DECLARE
	result INTEGER;
BEGIN
	result := a * b;
	RETURN result;
END;
$$ LANGUAGE plpgsql;


SELECT multiply_numbers();
SELECT multiply_numbers(2, 5);