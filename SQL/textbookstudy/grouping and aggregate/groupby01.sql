SELECT customer_id, count(*)
FROM rental
 GROUP BY customer_id