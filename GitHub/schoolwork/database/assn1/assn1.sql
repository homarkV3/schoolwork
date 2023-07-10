-- Active: 1688430322716@@127.0.0.1@3306
-- The commands below are used to recreate the university db for
-- both Postgresql and MySQL.
-- The scripts assume you are able to set your PATH variable either
-- in Linux, Mac or Windows. The PATH is used to allow execution from
-- the command prompt. You can also use a tool like pgadmin4 or
-- MySQL Workbench to create and populate the database
-- Backup the database to a file and restore it.
-- I supplied backup files and here are the commands for both Postgresql and MySQL
-- Create and populate the database (From CSV files)
-- MySQL
1. Open file and execute "create_university_db.sql"
2. Open file and execute "university_mysql.sql"
3. unzip "university_data_csv.sql" to a directory
4. Open file and execute "load_data_mysql.sql". You will need to update
the directory
-- PostgreSQL
-- 1. Open file and execute "create_university_db.sql"
-- 2. Open file and execute "university_postgres.sql"
-- 3. Unzip "university_data_csv.sql" to a directory
-- 4. Open file and execute "load_data_postgres.sql". You will need to
-- update the directory
-- Create and populate the database (From backup file)
1. Open file and execute "create_university_db.sql"
2. Use MySQL Workbench or pgadmin4 to load the appropriate backup file
