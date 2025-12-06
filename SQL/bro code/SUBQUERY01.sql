SELECT first_name, last_name, hourly_pay , 
-- SUBQUERY 
(SELECT AVG(hourly_pay) FROM employees) AS average

FROM employees;