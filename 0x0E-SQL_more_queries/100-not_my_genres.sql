-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT DISTINCT gen.name
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
INNER JOIN tv_genres AS gen
ON genres.genre_id = gen.id
WHERE gen.id NOT IN (
	SELECT gen.id
	FROM tv_shows AS shows
	INNER JOIN tv_show_genres AS genres
	ON shows.id = genres.show_id
	INNER JOIN tv_genres AS gen
	ON genres.genre_id = gen.id
	WHERE shows.title = "Dexter")
ORDER BY gen.name;
