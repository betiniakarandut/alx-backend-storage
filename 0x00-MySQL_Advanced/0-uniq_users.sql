-- 0-uniq_users.sql task

--Creates database holberton
CREATE DATABASE holberton;

--Creates a table called users
CREATE TABLE IF NOT EXISTS users(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, email VARCHAR (255) NOT NULL UNIQUE, name VARCHAR(255));
