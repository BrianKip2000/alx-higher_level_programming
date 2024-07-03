-- Create a states table
-- create a hbtn_0d_usa db
-- states has id: int primary key auto increment not null 
-- name varchar(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256)
	);
