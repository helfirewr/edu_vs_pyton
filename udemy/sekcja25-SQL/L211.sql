
SELECT * FROM cars ORDER BY id FETCH FIRST ROW ONLY; /* pierwszy wiersz */

SELECT * FROM cars ORDER BY id OFFSET 0 FETCH FIRST 3 ROW ONLY; /* rekordy z id 1, 2, 3 */

SELECT * FROM cars ORDER BY id OFFSET 3 FETCH FIRST 3 ROW ONLY; /* rekordy z id 4, 5, 6 */

SELECT * FROM cars ORDER BY id OFFSET 6 FETCH FIRST 3 ROW ONLY; /* Ostatnie 3 rekordy, w przykładzie zwróci dwa bo tyle tylko jest w bazie z id 7 i 8 */



