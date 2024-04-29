


/* LEFT JOIN zwróci wszystkie auta i ewentualnie kierowców powizanych z autem */
SELECT cars.id, cars.brand, cars.model, drivers.id as driver_id, drivers.name FROM cars LEFT JOIN drivers
ON cars.driver_id = drivers.id;

