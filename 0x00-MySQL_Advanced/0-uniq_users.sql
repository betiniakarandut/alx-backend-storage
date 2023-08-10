--Drop table if already created
DROP TABLE IF EXISTS users;
--Create table
CREATE TABLE IF NOT EXISTS users(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                   email VARCHAR (255) NOT NULL UNIQUE, 
                   name VARCHAR(255)
                  );
