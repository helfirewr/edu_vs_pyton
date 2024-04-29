
/* FULL JOIN zwraca wszystkie rekordy z obu tabel razem z parami i dane bez par */
SELECT cars.id, cars.brand, cars.model, drivers.id as driver_id, drivers.name FROM cars FULL JOIN drivers
ON cars.driver_id = drivers.id;