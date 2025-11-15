SELECT * FROM customers
-- WHERE last_name LIKE  "b%"
-- get all customers whose lastname starts with b
-- WHERE last_name LIKE  "%b%"
-- customers that have b somewhere in their last name 
-- WHERE last_name LIKE  "%y"
-- customers whose last name ends with y 
-- other pattern include "_______y" 5 underscores  means those customers with five letters before y, "b____y"
-- Excercise 
-- WHERE phone LIKE "%9"
-- WHERE phone NOT LIKE "%9"
WHERE address LIKE "%trail%" OR address LIKE "%avenue%"

