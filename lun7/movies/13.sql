SELECT count(DISTINCT name) FROM people JOIN stars ON
people.id=stars.person_id 
WHERE movie_id IN(SELECT movie_id FROM stars
JOIN people ON 
stars.person_id=people.id WHERE people.name='Kevin Bacon'and people.birth = 1958)
and name != 'Kevin Bacon';


  
/*SELECT count(DISTINCT name) FROM people JOIN stars ON
people.id=stars.person_id WHERE stars.movie_id (FROM stars JOIN people ON 
stars.person_id=people.id WHERE people.name='Kevin Bacon'and people.birth = 1958
& name != 'Kevin Bacon';176*/