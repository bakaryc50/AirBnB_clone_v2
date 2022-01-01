-- MySQL setup development
-- prepares a MySQL server for the project

-- Create a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev in localhost
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
