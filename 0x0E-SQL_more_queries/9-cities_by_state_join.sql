-- Write a script that lists all cities contained in the database hbtn_0d_usa

SELECT cs.id, cs.name, s.name FROM cities AS cs INNER JOIN states AS s ON cs.state_id = s.id ORDER BY cs.id;
