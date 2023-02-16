-- lists all shows contained in the database hbtn_0d_tvshows without a genre linked.
SELECT gen.name AS "genre", COUNT(shows.title) AS "number_of_shows"
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
INNER JOIN tv_genres AS gen
ON genres.genre_id = gen.id
GROUP BY gen.name
ORDER BY COUNT(shows.title) DESC;
