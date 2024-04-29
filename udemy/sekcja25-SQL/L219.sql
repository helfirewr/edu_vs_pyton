
SELECT COUNT(id) FROM cars; /* ilość rekordów w cars */

SELECT COUNT(id) AS num_cars FROM cars WHERE top_speed >= 200;
