-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT gen.name, SUM(ratings.rate) AS rating
FROM tv_show_genres AS genres
INNER JOIN tv_genres AS gen
ON genres.genre_id = gen.id 
INNER JOIN tv_show_ratings AS ratings
ON genres.show_id = ratings.show_id
GROUP BY gen.id
ORDER BY SUM(ratings.rate) DESC;
