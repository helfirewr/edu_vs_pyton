
CREATE OR REPLACE FUNCTION substract_numbers(a INT, b INT)
RETURNS INT AS $$
BEGIN
	RETURN a - b;
	END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION compute_num(a INT, b INT)
RETURNS TABLE (result INT) AS $$
DECLARE
	num INT;
BEGIN
	num := substract_numbers(a, b) + 10;
	num := num * 2;
	RETURN QUERY SELECT num;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM compute_num(5, 3);

