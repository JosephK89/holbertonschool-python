--Write a SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	email CHAR(255) UNIQUE NOT NULL,
	name CHAR(255),
	PRIMARY KEY(ID)
	);
