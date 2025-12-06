SELECT actor_id, count(*)
FROM film_actor
GROUP BY actor_id