SELECT title, rating
FROM film
WHERE rating NOT IN ( 'PG-13',  'R', 'NC-17')
-- this returns title and rating column that does not have PG-13, R, NC-17
 