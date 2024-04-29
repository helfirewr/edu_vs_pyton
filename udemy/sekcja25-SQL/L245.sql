CREATE OR REPLACE FUNCTION get_car_speed_type()
RETURNS TABLE(car_id INT, car_brand_model TEXT, car_speed_type TEXT) AS $$
DECLARE
	car_record cars%ROWTYPE;
BEGIN
	FOR car_record IN SELECT * FROM cars
	LOOP
		car_id := car_record.id;
		car_brand_model := CONCAT(car_record.brand, ' ', car_record.model);

		IF car_record.top_speed BETWEEN 100 AND 180 THEN
			car_speed_type := 'family car';
		ELSIF car_record.top_speed BETWEEN 180 AND 250 THEN
			car_speed_type := 'sports car';
		ELSIF car_record.top_speed > 250 THEN
			car_speed_type := 'super car';
		ELSE
			car_speed_type := 'unknown car';
		END IF;

		RETURN NEXT;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

