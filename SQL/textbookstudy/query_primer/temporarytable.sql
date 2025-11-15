CREATE TEMPORARY TABLE actors_j
(actor_id smallint(5),
first_name varchar(45),
last_name varchar(45)
);
 INSERT INTO actors_j
 SELECT actor_id, first_name, last_name
 FROM actor
 WHERE last_name LIKE "J%"