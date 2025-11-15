SELECT rental_id, rental_date, customer_id
FROM rental
WHERE return_date IS NULL
 OR return_date NOT BETWEEN '2005-05-01' AND '2005-09-01';