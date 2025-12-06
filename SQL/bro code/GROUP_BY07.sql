SELECT SUM(amount), customer_id
FROM trans03
GROUP BY customer_id
HAVING SUM(amount) > 1;