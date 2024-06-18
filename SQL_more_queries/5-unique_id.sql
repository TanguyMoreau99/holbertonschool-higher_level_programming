-- Create a table unique_id with two columns id (integer, default value: 1,
-- unique) and name (string), if he doesn't exist, in server
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
