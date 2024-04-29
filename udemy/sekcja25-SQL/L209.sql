
INSERT INTO public.cars(
	 brand, model, num_gears, top_speed)
	VALUES ('Ford', 'T', 3, 80),
	('BMW', 'M', 6, 260),
	('GMC', 'X1', 5, 170),
	('Renault', 'XB', 4, 190);

INSERT INTO public.cars(
	  brand, model, num_gears, top_speed )
	VALUES ('Pontiac', 'Firebird', NULL, 240);

SELECT * FROM cars LIMIT 3; /* pierwsze 3 */
SELECT * FROM cars ORDER BY id DESC LIMIT 3; /* ostatnie 3 ze względu na id */


SELECT * FROM cars ORDER BY id LIMIT 4 OFFSET 0; /* 4 pierwsze wyniki od id 1 do 4 */
SELECT * FROM cars ORDER BY id LIMIT 4 OFFSET 4; /* 4 pierwsze wyniki dla id od 5 do 8 */