SELECT title, rating FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2010 order by rating DESC, title;
SELECT COUNT(title) FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2010 order by rating DESC, title;