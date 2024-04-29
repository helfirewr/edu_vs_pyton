
CREATE OR REPLACE FUNCTION check_top_speed()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.top_speed < 0 THEN
		NEW.top_speed := 5;
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_speed
BEFORE INSERT OR UPDATE ON cars
FOR EACH ROW
EXECUTE PROCEDURE check_top_speed();

INSERT INTO public.cars(
	brand, model,  top_speed )
	VALUES ('Ford', 'Raptor', -10);


UPDATE cars SET top_speed = -50 WHERE id = 10;

SELECT * FROM cars;