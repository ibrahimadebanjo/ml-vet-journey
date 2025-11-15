SELECT rental_id, customer_id, rental_date
FROM rental
WHERE return_date IS NOT NULL