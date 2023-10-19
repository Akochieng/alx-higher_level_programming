-- lists all shows without the genre Comedy in the database
SELECT title FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT show_id
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy")
ORDER BY title ASC;
