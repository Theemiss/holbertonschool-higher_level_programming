-- create database and table 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id int NOT NULL , name varchar(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
