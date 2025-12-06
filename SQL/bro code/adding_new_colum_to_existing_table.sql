ALTER TABLE employees 
ADD COLUMN job  VARCHAR(25) AFTER hourly_pay;
SELECT * FROM employees