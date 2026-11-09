DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE person (person_id int PRIMARY KEY, last_name text, first_name text);
CREATE TABLE address (address_id int PRIMARY KEY, person_id int, city text, state text);

INSERT INTO person VALUES (1, 'Wang', 'Allen'), (2, 'Alice', 'Bob');
INSERT INTO address VALUES (1, 2, 'New York City', 'New York'), (2, 3, 'Leetcode', 'California');
