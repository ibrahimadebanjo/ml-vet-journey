SELECT order_id, o.customer_id, first_name, last_name 
FROM sql_store.orders o
JOIN sql_store.customers  c
ON o.customer_id = c.customer_id