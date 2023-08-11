-- Checks if table already created
--Create table if doesnt exist
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    `email` VARCHAR (255) NOT NULL UNIQUE, 
    `name` VARCHAR(255)
);
