SELECT * FROM sql_store.customers
-- WHERE last_name LIKE "%field%"
-- WHERE last_name REGEXP "^field"
-- WHERE last_name REGEXP "field$"
-- WHERE last_name REGEXP "^field|mac|rose"
-- WHERE last_name REGEXP "field$|mac|rose"
WHERE last_name REGEXP "field|mac|rose"
-- WHERE last_name REGEXP "[gim]e" 
-- WHERE last_name REGEXP "[a-h]e" 
-- WHERE last_name "ey$|on$"
-- ^ begining
-- $ end
-- | logical or
-- [abcd]
-- [a-f]


