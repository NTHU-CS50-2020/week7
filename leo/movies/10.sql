--list the names of all people who have directed a movie that received a rating of at least 9.0.
SELECT name FROM ratings JOIN directors ON ratings.movie_id = directors.movie_id
JOIN people ON directors.person_id = people.id
WHERE rating >= 9 GROUP BY name, person_id;