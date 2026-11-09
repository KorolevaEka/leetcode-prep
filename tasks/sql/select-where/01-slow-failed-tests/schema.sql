DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_name text, suite text, status text, duration_ms int);

INSERT INTO test_results VALUES
  (1, 'login_ok', 'auth', 'passed', 850),
  (2, 'login_bad_pwd', 'auth', 'failed', 2400),
  (3, 'logout', 'auth', 'passed', 300),
  (4, 'cart_add', 'cart', 'failed', 2000),
  (5, 'cart_checkout', 'cart', 'failed', 5100),
  (6, 'search_basic', 'search', 'passed', 2600),
  (7, 'search_empty', 'search', 'failed', 1200),
  (8, 'profile_edit', 'profile', 'skipped', 0),
  (9, 'export_csv', 'reports', 'failed', 3300);
