SELECT name FROM movies 
JOIN stars ON movies.id = stars.movie_id JOIN people ON stars.person_id = people.id 
WHERE year = 2004 GROUP BY name, person_id order by birth;

--cat 9.sql | sqlite3 movies.db | wc
