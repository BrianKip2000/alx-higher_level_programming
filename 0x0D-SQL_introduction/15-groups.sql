-- List tables with same values
SELECT score, COUNT(*) AS numbers FROM second_table GROUP BY score
