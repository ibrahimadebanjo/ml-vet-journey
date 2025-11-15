
-- SELECT 
-- first_name, 
-- last_name, 
-- points * 10 + 100 AS discount_factor
-- FROM customers

-- SELECT DISTINCT state FROM customers
-- SELECT first_name, last_name, (points * 10) + 100 FROM customers


-- WHERE customer_id = 1
-- ORDER BY first_name
SELECT name, unit_price, unit_price * 1.1 AS "new price" FROM products;