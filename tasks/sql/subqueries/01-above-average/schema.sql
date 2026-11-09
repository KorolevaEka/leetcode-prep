DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_name text, duration_ms int);

INSERT INTO test_results VALUES
  (1, 'login', 200),
  (2, 'logout', 300),
  (3, 'search', 600),
  (4, 'checkout', 700),
  (5, 'export', 800),
  (6, 'report', 1000);
