DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text, status text, started_at timestamp);

INSERT INTO test_runs VALUES
  (1, 'Staging', 'failed', '2024-03-01 09:00'),
  (2, 'staging', 'failed', '2024-03-04 14:30'),
  (3, 'prod', 'passed', '2024-03-02 10:00'),
  (4, 'PROD', 'failed', '2024-03-07 18:45'),
  (5, 'Local', 'failed', '2024-03-03 11:00'),
  (6, 'dev', 'failed', '2024-03-05 08:00'),
  (7, 'qa', 'failed', '2024-03-08 00:00'),
  (8, 'qa', 'passed', '2024-03-06 12:00'),
  (9, 'perf', 'failed', '2024-02-29 23:59'),
  (10, 'perf', 'passed', '2024-03-05 10:00'),
  (11, 'Canary', 'failed', '2024-03-03 03:00');
