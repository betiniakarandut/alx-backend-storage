-- Adds country to users to users table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country CHAR(2) ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);