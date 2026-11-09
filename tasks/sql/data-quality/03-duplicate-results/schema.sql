DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int REFERENCES test_runs, test_case_id int REFERENCES test_cases, status text, duration_ms int);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search');
INSERT INTO test_runs VALUES
  (1, 'staging'),
  (2, 'prod'),
  (3, 'staging');
INSERT INTO test_results VALUES
  (1, 1, 1, 'failed', 900),
  (2, 1, 1, 'passed', 850),
  (3, 1, 2, 'passed', 300),
  (4, 2, 1, 'passed', 410),
  (5, 2, 3, 'failed', 1500),
  (6, 2, 1, 'passed', 400),
  (9, 2, 1, 'failed', 395),
  (7, 3, 2, 'passed', 320),
  (8, 3, 3, 'passed', 1400),
  (10, 3, 3, 'passed', 1390);
