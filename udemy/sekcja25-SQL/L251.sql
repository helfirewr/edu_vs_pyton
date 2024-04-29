

ALTER TABLE cars ADD COLUMN updated TIMESTAMP;

CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
	NEW.updated := NOW();
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_car_timestamp
BEFORE UPDATE ON cars
FOR EACH ROW
EXECUTE PROCEDURE update_timestamp();



UPDATE cars SET top_speed = -40 WHERE id = 10;

SELECT * FROM cars;


