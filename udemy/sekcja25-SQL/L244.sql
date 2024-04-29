CREATE OR EPLACE FUNCTION get_car_type()
RETURNS TABLE(car_id INT, car_brand_model TEXT, car_type TEXT) AS $$
BEGIN
	RETURN QUERY SELECT id, CONCAT(brand, ' ', model),
	CASE
		WHEN model = 'Viper' THEN 'sports car'
		WHEN model = 'Ram' THEN 'truck'
		WHEN model = 'w140' THEN 'family car'
		ELSE 'unknown car'
	END
	FROM cars;
END;
$$ LANGUAGE plpgsql;

