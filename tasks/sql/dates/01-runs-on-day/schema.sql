DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_runs (test_run_id int PRIMARY KEY, env text, started_at timestamp);

INSERT INTO test_runs VALUES
  (1, 'prod', '2024-03-04 23:59:59'),
  (2, 'staging', '2024-03-05 00:00:00'),
  (3, 'prod', '2024-03-05 09:15:00'),
  (4, 'qa', '2024-03-05 23:59:59'),
  (5, 'prod', '2024-03-06 00:00:00'),
  (6, 'staging', '2024-03-06 08:00:00');
