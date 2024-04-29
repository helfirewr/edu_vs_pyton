
/* utworzenie własnego typu z określonymi wartościami */
CREATE TYPE car_color AS ENUM('red', 'blue', 'white', 'yellow', 'black', 'green');

ALTER TABLE cars ADD color car_color DEFAULT 'red';



