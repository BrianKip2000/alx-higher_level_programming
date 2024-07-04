-- Create database hbtn_0d_usa 
-- Create table cities
-- has id: INT UNIQUE AUTO-GENERATED NOT NULL AND IS PRIMARY KEY
-- state_id: INT NOT NULL FOREIGN KEY
-- name: VArchar (256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
 	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
	);
