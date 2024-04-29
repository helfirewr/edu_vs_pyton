CREATE OR REPLACE FUNCTION get_even_id_cars()
RETURNS TABLE (car_id INT, car_brand_model TEXT, car_num_gears SMALLINT, car_top_speed NUMERIC) AS $$
DECLARE
	car_record cars%ROWTYPE;
BEGIN
	FOR car_record IN SELECT * FROM cars
	LOOP
		IF car_record.id % 2 = 0 THEN
			car_id := car_record.id;
			car_brand_model := CONCAT(car_record.brand, ' ', car_record.model);
			car_num_gears := car_record.num_gears;
			car_top_speed := car_record.top_speed;
			RETURN NEXT;
		END IF;
	END LOOP;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_even_id_cars();
