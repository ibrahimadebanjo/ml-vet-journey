SELECT customer.first_name, customer.last_name,
 time(rental.rental_date) rental_time
FROM customer
INNER JOIN rental

ON customer.customer_id = rental.customer_id
WHERE date(rental.rental_date) = '2005-06-14';
