SELECT DISTINCT name FROM people
JOIN directors on people.id = directors.person_id
JOIN movies ON directors.movie_id = movies.id
JOIN ratings on movies.id = ratings.movie_id
WHERE ratings.rating >= 9;
-- 另一種
SELECT DISTINCT name FROM people WHERE id IN(
SELECT person_id FROM directors WHERE movie_id IN(
SELECT movie_id FROM ratings WHERE rating >= 9
));