-- Create a user called user_0d_1 
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'User_0d_1_pwd';
-- Grant all priveledges on user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
