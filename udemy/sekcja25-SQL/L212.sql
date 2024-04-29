

INSERT INTO public.cars(
	  brand, model, num_gears, top_speed )
	VALUES ('Pontiac', 'Firebird', NULL, 240);


SELECT * FROM cars WHERE num_gears IS NULL ;

SELECT * FROM cars WHERE NOT num_gears IS NULL ;