DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_case_id int REFERENCES test_cases, status text, executed_at timestamp);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search');
INSERT INTO test_results VALUES
  (1, 1, 'failed', '2024-03-02 10:00'),
  (2, 1, 'failed', '2024-03-01 09:00'),
  (3, 2, 'passed', '2024-03-01 12:00'),
  (4, 2, 'failed', '2024-03-02 12:00'),
  (5, 1, 'passed', '2024-03-03 08:00'),
  (6, 3, 'passed', '2024-03-05 10:00'),
  (7, 3, 'failed', '2024-03-01 10:00'),
  (8, 3, 'passed', '2024-03-09 10:00');
