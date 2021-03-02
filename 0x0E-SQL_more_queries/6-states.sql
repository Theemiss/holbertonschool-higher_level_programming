-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id int UNIQUE PRIMARY KEY AUTO_INCREMENT, name varchar(256) NOT NULL); 
