DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE builds (build_id int PRIMARY KEY, version text, built_on date);
CREATE TABLE test_runs (test_run_id int PRIMARY KEY, build_id int REFERENCES builds);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_run_id int REFERENCES test_runs, status text);

INSERT INTO builds VALUES
  (1, '2.0.0', '2024-02-01'),
  (2, '2.0.1', '2024-02-08'),
  (3, '2.1.0', '2024-02-15'),
  (4, '2.1.1', '2024-02-22');
INSERT INTO test_runs VALUES
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 3),
  (5, 3);
INSERT INTO test_results VALUES
  (1, 1, 'passed'),
  (2, 1, 'failed'),
  (3, 2, 'failed'),
  (4, 2, 'failed'),
  (5, 3, 'passed'),
  (6, 3, 'passed'),
  (7, 4, 'failed'),
  (8, 5, 'passed'),
  (9, 5, 'skipped');
