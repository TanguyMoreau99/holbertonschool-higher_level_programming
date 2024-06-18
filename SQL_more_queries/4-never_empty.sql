-- Create a table id_not_null with two columns id (integer, default value: 1)
-- and name (string), if he doesn't exist, in server
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
