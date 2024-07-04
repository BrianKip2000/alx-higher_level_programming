-- List all shows in the database
-- SELECT sh.title, ge.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres ge ON sh.id=ge.genre_id ORDER BY sh.title, ge.genre_id;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
