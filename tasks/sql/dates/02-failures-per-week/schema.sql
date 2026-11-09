DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_name text, status text, executed_at timestamp);

INSERT INTO test_results VALUES
  (1, 'login', 'failed', '2024-03-01 10:00'),
  (2, 'login', 'passed', '2024-03-02 10:00'),
  (3, 'cart', 'failed', '2024-03-03 23:30'),
  (4, 'cart', 'failed', '2024-03-04 00:05'),
  (5, 'search', 'passed', '2024-03-05 12:00'),
  (6, 'search', 'failed', '2024-03-08 09:00'),
  (7, 'export', 'failed', '2024-03-10 23:50'),
  (8, 'login', 'failed', '2024-03-11 08:00'),
  (9, 'cart', 'failed', '2024-03-12 14:00'),
  (10, 'export', 'passed', '2024-03-12 15:00'),
  (11, 'search', 'failed', '2024-03-13 16:30');
