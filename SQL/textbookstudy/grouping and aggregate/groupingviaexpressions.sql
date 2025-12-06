	SELECT extract(YEAR FROM rental_date) year,
    COUNT(*) how_many
    FROM rental
    GROUP BY extract(YEAR FROM rental_date)