-- Showing details of a specific table
USE hbtn_0c_0;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, CHARACTER_SET, COLLATION, EXTRA
FROM information_schema.columns
WHERE table_name = 'first_table'
ORDER BY ORDINAL_POSITION;
