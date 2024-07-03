-- Create a table if not exists
-- unique_id default 1, unique
-- name Varchar(256)
CREATE TABLE IF NOT EXISTS unique_id (
	id INT default 1 UNIQUE,
	name VARCHAR(256)
	);
