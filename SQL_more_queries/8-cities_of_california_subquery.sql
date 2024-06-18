-- List all the cities of the state of California
-- that can be found in the database hbtn_0e_0_usa
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California") 
ORDER BY id ASC;