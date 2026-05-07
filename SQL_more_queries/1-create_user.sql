-- Creates the user user_0d_1 with the password user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases and tables to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flushes privileges to ensure that the changes take effect immediately
FLUSH PRIVILEGES;
