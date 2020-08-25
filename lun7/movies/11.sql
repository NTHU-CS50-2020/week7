SELECT title FROM movies WHERE id
IN(SELECT movie_id FROM ratings WHERE movie_id
IN(SELECT movie_id FROM stars WHERE person_id
IN(SELECT id from people where name='Chadwick Boseman'))
ORDER BY -rating LIMIT 5);