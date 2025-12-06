SELECT MAX(amount) max_amt,
MIN(amount),
AVG(amount),
SUM(amount),
COUNT(*) num_payments
FROM payment;