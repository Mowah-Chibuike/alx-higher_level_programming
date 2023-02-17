-- lists all shows from hbtn_0d_tvshows_rate by their ratings
SELECT shows.title, SUM(ratings.rate) AS rating
FROM tv_shows AS shows
INNER JOIN tv_show_ratings AS ratings
ON shows.id = ratings.show_id 
GROUP BY shows.id
ORDER BY SUM(ratings.rate) DESC;
