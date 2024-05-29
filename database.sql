CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;
CREATE TABLE IF NOT EXISTS whats_mess (
    name VARCHAR(100) NOT NULL,
    phone_number varchar(13) PRIMARY KEY
);
INSERT INTO whats_mess (name, phone_number) VALUES
    ('<name>', '<country code><phone number>'),
    
select * from whats_mess;
