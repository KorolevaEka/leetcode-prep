DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, suite text, name text, duration_ms int);

INSERT INTO test_cases VALUES
  (1, 'auth', 'login', 1200),
  (2, 'auth', 'register', 900),
  (3, 'auth', 'logout', 900),
  (4, 'auth', 'reset', 300),
  (5, 'cart', 'add', 700),
  (6, 'cart', 'remove', 200),
  (7, 'cart', 'checkout', 2500),
  (8, 'cart', 'coupon', 100),
  (9, 'search', 'basic', 150),
  (10, 'reports', 'export', 3000),
  (11, 'reports', 'import', 3000),
  (12, 'reports', 'view', 100);
