SELECT title FROM movies
JOIN stars on stars.movie_id = movies.id
JOIN people on people.id = stars.person_id
WHERE people.name = 'Johnny Depp' AND title IN(
SELECT title FROM movies
JOIN stars on stars.movie_id = movies.id
JOIN people on people.id = stars.person_id
WHERE people.name = 'Helena Bonham Carter');