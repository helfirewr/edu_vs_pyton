ALTER TABLE cars ADD price NUMERIC(10,2) DEFAULT 50000;
ALTER TABLE cars ADD color VARCHAR(12) DEFAULT 'red';
ALTER TABLE cars DROP COLUMN color;