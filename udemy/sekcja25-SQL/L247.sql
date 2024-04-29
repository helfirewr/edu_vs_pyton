CREATE OR REPLACE FUNCTION get_cars_by_ids(ids INT[])
RETURNS TABLE(car_id INT, car_brand_model TEXT, car_num_gears SMALLINT, car_top_speed NUMERIC) AS $$
DECLARE
	current_id INT;
BEGIN
	FOREACH current_id IN ARRAY ids
	LOOP
		RETURN QUERY SELECT id, CONCAT(brand, ' ', model), num_gears, top_speed
		FROM cars WHERE id = current_id;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_cars_by_ids(ARRAY[1, 3, 4, 6]);