DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_case_id int REFERENCES test_cases, env text, duration_ms int);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search'),
  (4, 'export');
INSERT INTO test_results VALUES
  (1, 1, 'staging', 400),
  (2, 1, 'staging', 450),
  (3, 2, 'staging', 1200),
  (4, 3, 'staging', 300),
  (5, 1, 'prod', 380),
  (6, 2, 'prod', 1500),
  (7, 2, 'prod', 1400),
  (8, 2, 'prod', 1600),
  (9, 4, 'prod', 90),
  (10, 1, 'qa', 500),
  (11, 3, 'qa', 700),
  (12, 3, 'qa', 650);
