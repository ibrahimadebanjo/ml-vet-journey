SELECT title, rating
FROM film
WHERE rating IN (
SELECT rating FROM film WHERE title LIKE '%PET%')
