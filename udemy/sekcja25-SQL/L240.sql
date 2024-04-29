CREATE OR REPLACE FUNCTION add_car_and_driver(car_brand VARCHAR, car_model VARCHAR, driver_name VARCHAR)
RETURNS VOID AS $$
DECLARE
	driver_id INTEGER;
BEGIN
	SELECT id INTO driver_id FROM drivers WHERE name = driver_name;

	IF driver_id IS NULL THEN
		INSERT INTO drivers (name) VALUES (driver_name) RETURNING id INTO driver_id;
	END IF;

	INSERT INTO cars (brand, model, driver_id) VALUES (car_brand, car_model, driver_id);
END;
$$ LANGUAGE plpgsql;


SELECT add_car_and_driver('Mazda', 'Miata', 'Ksawery');

