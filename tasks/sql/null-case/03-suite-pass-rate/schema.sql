DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_results (test_result_id int PRIMARY KEY, suite text, test_name text, status text);

INSERT INTO test_results VALUES
  (1, 'auth', 'login', 'passed'),
  (2, 'auth', 'logout', 'passed'),
  (3, 'auth', 'register', 'failed'),
  (4, 'auth', 'reset', 'passed'),
  (5, 'auth', 'sso', 'skipped'),
  (6, 'cart', 'add', 'passed'),
  (7, 'cart', 'remove', 'failed'),
  (8, 'legacy', 'old_a', 'skipped'),
  (9, 'legacy', 'old_b', 'skipped'),
  (10, 'legacy', 'old_c', 'skipped'),
  (11, 'reports', 'export', 'passed'),
  (12, 'reports', 'import', 'passed'),
  (13, 'reports', 'view', 'passed'),
  (14, 'reports', 'print', 'passed'),
  (15, 'search', 'basic', 'failed'),
  (16, 'search', 'empty', 'failed'),
  (17, 'search', 'fuzzy', 'skipped'),
  (18, 'search', 'sort', NULL);
