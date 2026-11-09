DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE builds (build_id int PRIMARY KEY, version text);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, build_id int REFERENCES builds);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int REFERENCES test_runs, status text);

INSERT INTO builds VALUES
  (1, '3.0.0'),
  (2, '3.0.1'),
  (3, '3.1.0'),
  (4, '3.1.1');
INSERT INTO test_runs VALUES
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 3),
  (5, 4);
INSERT INTO test_results VALUES
  (1, 1, 'passed'),
  (2, 1, 'passed'),
  (3, 1, 'passed'),
  (4, 1, 'passed'),
  (5, 1, 'failed'),
  (6, 2, 'passed'),
  (7, 2, 'passed'),
  (8, 2, 'skipped'),
  (9, 3, 'passed'),
  (10, 3, 'passed'),
  (11, 3, 'passed'),
  (12, 3, 'passed'),
  (13, 4, 'passed'),
  (14, 4, 'failed'),
  (15, 4, 'failed'),
  (16, 4, 'failed'),
  (17, 4, 'skipped'),
  (18, 5, 'passed'),
  (19, 5, 'passed'),
  (20, 5, 'passed'),
  (21, 5, 'passed'),
  (22, 5, 'passed'),
  (23, 5, 'passed'),
  (24, 5, 'passed'),
  (25, 5, 'failed'),
  (26, 5, 'skipped'),
  (27, 5, 'skipped');
