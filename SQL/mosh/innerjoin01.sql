SELECT * FROM sql_store.orders 
JOIN sql_store.customers  
ON orders.customer_id = customers.customer_id
