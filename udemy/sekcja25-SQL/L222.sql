
SELECT COUNT(id), brand FROM cars GROUP BY brand HAVING COUNT(id) >= 2;
/* zwraca ilość samochodów w ramach producentów którzy przynajmniej mają 2 rekordy
   w bazie */