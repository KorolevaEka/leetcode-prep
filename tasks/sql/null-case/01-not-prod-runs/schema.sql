DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text, status text);

INSERT INTO test_runs VALUES
  (1, 'prod', 'passed'),
  (2, 'staging', 'failed'),
  (3, NULL, 'passed'),
  (4, 'prod', 'failed'),
  (5, 'qa', 'passed'),
  (6, NULL, 'failed'),
  (7, 'prod', 'passed');
