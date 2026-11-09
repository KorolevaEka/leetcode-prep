DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_case_id int REFERENCES test_cases, status text, executed_at timestamp);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search'),
  (4, 'export'),
  (5, 'profile'),
  (6, 'reports'),
  (7, 'settings');
INSERT INTO test_results VALUES
  (10, 1, 'passed', '2024-03-01 10:00'),
  (3, 1, 'failed', '2024-03-05 10:00'),
  (4, 2, 'failed', '2024-03-02 11:00'),
  (11, 2, 'passed', '2024-03-06 11:00'),
  (5, 3, 'failed', '2024-03-03 09:00'),
  (1, 3, 'failed', '2024-03-07 09:00'),
  (2, 4, 'passed', '2024-03-04 12:00'),
  (6, 5, 'failed', '2024-03-01 13:00'),
  (7, 5, 'failed', '2024-03-02 13:00'),
  (8, 5, 'passed', '2024-03-03 13:00'),
  (9, 7, 'failed', '2024-03-08 15:00'),
  (12, 7, 'passed', '2024-03-02 15:00');
