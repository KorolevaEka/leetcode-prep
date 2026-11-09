DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE builds (build_id int PRIMARY KEY, version text);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, build_id int REFERENCES builds, env text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int REFERENCES test_runs, test_name text, status text);

INSERT INTO builds VALUES
  (1, '1.4.0'),
  (2, '1.4.1'),
  (3, '1.5.0');
INSERT INTO test_runs VALUES
  (1, 1, 'staging'),
  (2, 1, 'prod'),
  (3, 2, 'staging'),
  (4, 3, 'staging');
INSERT INTO test_results VALUES
  (1, 1, 'login', 'passed'),
  (2, 1, 'checkout', 'failed'),
  (3, 2, 'login', 'passed'),
  (4, 3, 'search', 'failed'),
  (5, 3, 'checkout', 'failed'),
  (6, 4, 'login', 'passed'),
  (7, 2, 'export', 'failed'),
  (8, 4, 'profile', 'failed');
