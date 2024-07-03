-- Create a databse for hbtn
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user called user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
-- Grant select on the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FlUSH PRIVILEGES;
