CREATE OR REPLACE FUNCTION get_cars_by_driver(driver_name VARCHAR)
RETURNS TABLE(id INTEGER, brand VARCHAR, model VARCHAR) AS $$
BEGIN
	RETURN QUERY
	SELECT c.id, c.brand, c.model
	FROM cars c
	JOIN drivers d ON c.driver_id = d.id
	WHERE d.name = driver_name;
END;
$$ LANGUAGE plpgsql;



SELECT * FROM get_cars_by_driver('Monika');

