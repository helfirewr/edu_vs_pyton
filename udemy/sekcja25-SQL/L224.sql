
/* Wszystkie auta któryś prędkość jest mniejsza od
   średniej prędkości wszystkich aut w cars */
SELECT * FROM cars WHERE top_speed < ( SELECT AVG(top_speed) FROM cars ) ;

