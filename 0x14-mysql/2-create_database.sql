-- This script create database tyrell_corp
create database IF NOT EXISTS tyrell_corp;
use tyrell_corp;
create table IF NOT EXISTS nexus6 (id int, name varchar(255));
insert into nexus6(id, name) VALUES (1, 'Leon');
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost'
