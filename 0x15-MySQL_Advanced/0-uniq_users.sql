--Write a SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email CHAR(255) UNIQUE NOT NULL,
	name CHAR(255));
