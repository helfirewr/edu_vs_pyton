
/* Zwraca auta z 6 biegami i top speed 200 lub więcej, uwaga bez duplikatów */
SELECT * FROM cars WHERE num_gears = 6
UNION
SELECT * FROM cars WHERE top_speed >= 200;


/* To samo co wyżej ale z duplikatami */
SELECT * FROM cars WHERE num_gears = 6
UNION ALL
SELECT * FROM cars WHERE top_speed >= 200;
