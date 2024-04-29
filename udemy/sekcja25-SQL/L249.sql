
CREATE OR REPLACE FUNCTION get_cars_by_ids3(ids INT[])
RETURNS TABLE(car_id INT, car_top_speed NUMERIC) AS $$
DECLARE
	current_id INT;
	max_id INT;
BEGIN
	SELECT MAX(id) INTO max_id FROM cars;

	FOREACH current_id IN ARRAY ids
	LOOP
		EXIT WHEN current_id <= 0;

		IF current_id > max_id THEN
			EXIT;
		END IF;

		RETURN QUERY SELECT id, top_speed FROM cars WHERE id = current_id;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_cars_by_ids3(ARRAY[1,2,-3, 1000]);

