SELECT fa.actor_id, f.rating, COUNT(*)
FROM film_actor fa
INNER JOIN film f
ON fa. film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY fa.actor_id, f.rating
HAVING count(*) > 9;