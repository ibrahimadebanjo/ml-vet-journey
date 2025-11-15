SELECT c.first_name, c.last_name,
 time(r.rental_date) rental_time
FROM customer AS c
INNER JOIN rental AS r

ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14';
