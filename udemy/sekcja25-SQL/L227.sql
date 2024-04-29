CREATE TABLE IF NOT EXISTS drivers (
	id SERIAL PRIMARY KEY,
	name varchar(16) NOT NULL
);

INSERT INTO public.drivers(
	  name)
	VALUES ('Monika'), ('Adam'), ('Kasia'), ('Karol');


ALTER TABLE cars ADD COLUMN driver_id INTEGER REFERENCES drivers(id);