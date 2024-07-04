-- List all shows in the database
SELECT sh.title, ge.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres ge ON sh.id=ge.genre_id ORDER BY sh.title, ge.genre_id;
