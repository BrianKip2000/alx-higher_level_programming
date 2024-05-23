-- Listing without those without names
SELECT score, name FROM second_table WHERE name IS NOT NULL OR name != '' ORDER BY score DESC;
