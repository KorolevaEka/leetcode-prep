DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int REFERENCES test_runs, test_case_id int REFERENCES test_cases, status text);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search'),
  (4, 'export');
INSERT INTO test_runs VALUES
  (1, 'staging'),
  (2, 'staging'),
  (3, 'prod'),
  (4, 'staging'),
  (5, 'prod');
INSERT INTO test_results VALUES
  (1, 1, 1, 'failed'),
  (2, 1, 2, 'failed'),
  (3, 1, 3, 'failed'),
  (4, 2, 1, 'failed'),
  (5, 2, 2, 'failed'),
  (6, 3, 1, 'passed'),
  (7, 3, 2, 'failed'),
  (8, 3, 3, 'failed'),
  (9, 4, 1, 'failed'),
  (10, 4, 2, 'failed'),
  (11, 4, 4, 'failed'),
  (12, 5, 1, 'passed'),
  (13, 5, 2, 'passed'),
  (14, 5, 3, 'failed'),
  (15, 5, 4, 'failed'),
  (16, 2, 3, 'passed');
