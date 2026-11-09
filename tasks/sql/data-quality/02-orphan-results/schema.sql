DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int, test_name text, status text);

INSERT INTO test_runs VALUES
  (1, 'staging'),
  (2, 'prod'),
  (3, 'staging'),
  (4, 'qa');
INSERT INTO test_results VALUES
  (1, 1, 'login', 'passed'),
  (2, 2, 'login', 'failed'),
  (3, 9, 'cart', 'passed'),
  (4, NULL, 'search', 'passed'),
  (5, 3, 'export', 'failed'),
  (6, 7, 'profile', 'passed'),
  (7, 4, 'reports', 'passed'),
  (8, 9, 'settings', 'failed');
