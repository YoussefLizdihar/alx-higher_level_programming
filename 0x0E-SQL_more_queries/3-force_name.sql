-- This script creates a table named 'force_name' in the specified MySQL database if it doesn't already exist.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
