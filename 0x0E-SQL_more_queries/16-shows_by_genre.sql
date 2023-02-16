-- lists all shows contained in the database hbtn_0d_tvshows without a genre linked.
SELECT shows.title, gen.name
FROM tv_shows AS shows
LEFT OUTER JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
LEFT OUTER JOIN tv_genres AS gen
ON genres.genre_id = gen.id
ORDER BY shows.title, gen.name;
