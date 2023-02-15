-- displays the max temperature of each state (ordered by State name).
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT state, MAX(value) as "max_temp"
FROM temperatures
GROUP BY state
ORDER BY state;
