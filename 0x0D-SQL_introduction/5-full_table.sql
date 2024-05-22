-- Showing details of a specific table
SELECT
	COLUMN_NAME,
	COLUMN_TYPE,
	IS_NULLABLE,
	COLUMN_KEY,
	COLUMN_DEFAULT,
	EXTRA
FROM
	information_schema.COLUMNS
WHERE
	TABLE_SCHEMA = 'hbtn_0c_0'
	AND TABLE_NAME = 'first_table'
