-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT city, AVG(value) as "avg_temp"
FROM temperatures 
GROUP BY city 
ORDER BY AVG(value) DESC;
