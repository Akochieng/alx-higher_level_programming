-- lists all genres from tv shows and displays the number of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.id, tv_genres.name;
