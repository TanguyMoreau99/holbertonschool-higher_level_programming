-- Create a database hbtn_0d_usa if doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create a table cities with three columns id (integer, unique, auto generated,
-- not null and primary key), state_id (integer, not null, second key for id in states)
-- and name (string, not null) if he doesn't exist
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);