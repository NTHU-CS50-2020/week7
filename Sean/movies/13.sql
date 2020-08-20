SELECT DISTINCT name FROM people
WHERE name != 'Kevin Bacon' and id IN(
SELECT person_id FROM stars WHERE movie_id IN(
SELECT movie_id from stars WHERE person_id IN(
SELECT id FROM people WHERE name IS 'Kevin Bacon' and birth = 1958)));