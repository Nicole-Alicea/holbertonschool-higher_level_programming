-- Script that creates a database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT UNIQUE AUTO NOT NULL PRIMARY KEY,
name VARCHAR(256) NOT NULL);