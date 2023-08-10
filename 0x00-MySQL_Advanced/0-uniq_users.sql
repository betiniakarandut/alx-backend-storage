-- Checks if table already created
IF NOT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema = 'holberton' AND table_name = 'users') THEN
    --Create table if doesnt exist
    CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
	email VARCHAR (255) NOT NULL UNIQUE, 
	name VARCHAR(255)
    );
END IF;
