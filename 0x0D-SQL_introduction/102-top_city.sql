-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT city, AVG(value) as "avg_temp"
FROM temperatures 
WHERE month BETWEEN 7 AND 8
GROUP BY city 
ORDER BY AVG(value) DESC
LIMIT 3;
