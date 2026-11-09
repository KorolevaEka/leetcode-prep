DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text, suite text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_case_id int REFERENCES test_cases, status text);

INSERT INTO test_cases VALUES
  (1, 'login', 'auth'),
  (2, 'logout', 'auth'),
  (3, 'add_to_cart', 'cart'),
  (4, 'checkout', 'cart'),
  (5, 'export_csv', 'reports'),
  (6, 'reset_password', 'auth');
INSERT INTO test_results VALUES
  (1, 1, 'passed'),
  (2, 1, 'failed'),
  (3, 2, 'passed'),
  (4, 4, 'failed'),
  (5, 4, 'passed'),
  (6, 5, NULL);
