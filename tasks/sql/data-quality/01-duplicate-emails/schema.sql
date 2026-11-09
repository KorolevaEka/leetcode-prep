DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE users (user_id int PRIMARY KEY, email text, created_at date);

INSERT INTO users VALUES
  (1, 'qa.bot@example.com', '2024-01-10'),
  (2, 'QA.Bot@example.com', '2024-01-11'),
  (3, 'dev1@example.com', '2024-01-12'),
  (4, 'dev2@example.com', '2024-01-12'),
  (5, 'dev1@example.com', '2024-01-15'),
  (6, 'dev1@example.com', '2024-01-20'),
  (7, 'ops@example.com', '2024-02-01');
