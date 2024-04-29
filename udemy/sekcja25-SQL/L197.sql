CREATE TABLE IF NOT EXISTS cars (
	id SERIAL PRIMARY KEY,
	brand VARCHAR(24) NOT NULL,
	model VARCHAR(24) NOT NULL,
	num_gears smallint DEFAULT 4,
	top_speed NUMERIC(7,3), /* 345.123 */
	production_date DATE default CURRENT_DATE,
	created timestamp default CURRENT_TIMESTAMP
);