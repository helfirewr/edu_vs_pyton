CREATE OR REPLACE FUNCTION add_car(brand VARCHAR, model VARCHAR)
RETURNS VOID AS $$
DECLARE
	top_speed INTEGER := (100 + floor(random() * 151))::integer;
BEGIN
	INSERT INTO cars (brand, model, top_speed) VALUES (brand, model, top_speed);
END;
$$ LANGUAGE plpgsql;


SELECT add_car('Toyota', 'Corolla');