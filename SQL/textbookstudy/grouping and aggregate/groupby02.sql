SELECT customer_id, count(*)
FROM rental
GROUP BY customer_id
ORDER BY 2 DESC