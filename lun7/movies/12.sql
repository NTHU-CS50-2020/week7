SELECT title 
FROM movies JOIN stars 
on movies.id=stars.movie_id 
JOIN people 
on stars.person_id=people.id 
WHERE people.name = 'Johnny Depp' 
AND title IN(
SELECT title 
FROM movies JOIN stars 
on movies.id=stars.movie_id 
JOIN people 
on stars.person_id=people.id 
WHERE people.name = 'Helena Bonham Carter');