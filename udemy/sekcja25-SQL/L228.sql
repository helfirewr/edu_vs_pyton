


/* INNER JOIN zwróci tylko te dane które pasują ze sobą, czyli jesli
auto ma null jako driver_id to ten rekord nie będzie zwrócony */
SELECT cars.id, cars.brand, cars.model, drivers.id as driver_id, drivers.name FROM cars INNER JOIN drivers
ON cars.driver_id = drivers.id;