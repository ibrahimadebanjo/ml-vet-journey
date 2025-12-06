SELECT COUNT(customer_id) num_rows,
COUNT( DISTINCT customer_id) num_customers
FROM payment;