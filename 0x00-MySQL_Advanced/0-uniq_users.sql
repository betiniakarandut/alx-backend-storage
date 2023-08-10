--Creates a table called users
IF NOT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema = 'holberton' AND table_name = 'users') THEN
	CREATE TABLE users(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                           email VARCHAR (255) NOT NULL UNIQUE, 
                           name VARCHAR(255)
                          );
