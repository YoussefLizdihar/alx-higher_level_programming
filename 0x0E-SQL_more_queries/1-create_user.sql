-- This script creates a MySQL server user named user_0d_1 with all privileges
-- on the MySQL server. If the user already exists, it will not fail.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
