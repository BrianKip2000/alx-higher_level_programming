-- List tables with same values
SELECT score, COUNT(score) AS numbers FROM second_table GROUP BY score ORDER BY score DESC;
