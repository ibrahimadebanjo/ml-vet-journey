SELECT first_name, last_name FROM customers
WHERE customer_id NOT IN
(SELECT DISTINCT customer_id FROM trans03
WHERE customer_id IS NOT NULL)