SELECT name FROM people WHERE people.id IN
(
    SELECT DISTINCT(stars.person_id) FROM
    stars JOIN movies on stars.movie_id = movies.id
    WHERE movies.year = 2004
)
/*
https://stackoverflow.com/questions/59664139/why-is-this-sql-query-not-working-cs50-pset7-movies
