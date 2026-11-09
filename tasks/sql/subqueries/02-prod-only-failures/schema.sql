DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE builds (build_id int PRIMARY KEY, version text);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, build_id int REFERENCES builds, env text, status text);

INSERT INTO builds VALUES
  (1, '5.0.0'),
  (2, '5.0.1'),
  (3, '5.1.0'),
  (4, '5.1.1');
INSERT INTO test_runs VALUES
  (1, 1, 'prod', 'failed'),
  (2, 1, 'staging', 'passed'),
  (3, 2, 'prod', 'failed'),
  (4, 2, 'prod', 'passed'),
  (5, 3, 'prod', 'passed'),
  (6, 4, 'prod', 'failed'),
  (7, NULL, 'staging', 'failed'),
  (8, 4, 'qa', 'failed');
