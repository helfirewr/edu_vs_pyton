
/* RIGHT JOIN zwróci wszystkich kierowców z drivers i ewentualnie
   samochody z którymi są powiązani */
SELECT cars.id, cars.brand, cars.model, drivers.id as driver_id, drivers.name FROM cars RIGHT JOIN drivers
ON cars.driver_id = drivers.id;