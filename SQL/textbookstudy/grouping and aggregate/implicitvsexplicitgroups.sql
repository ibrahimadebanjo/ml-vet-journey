SELECT customer_id,
MIN(amount) min_amt,
MAX(amount) max_amt,
AVG(amount) avg_amt,
SUM(amount) total_amt,
COUNT(amount) num_payments
FROM payment
GROUP BY customer_id;
