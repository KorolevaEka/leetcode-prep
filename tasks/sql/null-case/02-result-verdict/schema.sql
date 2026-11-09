DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_name text, status text, retries int);

INSERT INTO test_results VALUES
  (1, 'login', 'passed', 0),
  (2, 'cart', 'passed', 2),
  (3, 'search', 'passed', NULL),
  (4, 'export', 'failed', 3),
  (5, 'profile', 'failed', NULL),
  (6, 'legacy', 'skipped', NULL),
  (7, 'reports', NULL, NULL),
  (8, 'settings', 'passed', 1);
