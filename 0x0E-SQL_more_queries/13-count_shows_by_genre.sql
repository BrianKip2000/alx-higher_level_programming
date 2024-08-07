-- use hbtn_0d_tvshows;
-- -- Link where genre id is unmatched
-- SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id GROUP BY tv_genres.name HAVING COUNT(tv_show_genres.show_id) > 0 ORDER BY number_of_shows DESC;
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows 
FROM tv_genres 
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id 
GROUP BY tv_genres.name 
HAVING COUNT(tv_show_genres.show_id) > 0 
ORDER BY number_of_shows DESC;
