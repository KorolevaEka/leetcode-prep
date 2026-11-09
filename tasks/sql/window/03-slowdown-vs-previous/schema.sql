DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE builds (build_id int PRIMARY KEY, version text, built_on date);
CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, build_id int REFERENCES builds, test_case_id int REFERENCES test_cases, duration_ms int);

INSERT INTO builds VALUES
  (1, '4.0', '2024-01-10'),
  (2, '4.1', '2024-01-24'),
  (3, '4.2', '2024-02-07');
INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search');
INSERT INTO test_results VALUES
  (1, 1, 1, 100),
  (2, 2, 1, 150),
  (3, 3, 1, 160),
  (4, 1, 2, 400),
  (5, 2, 2, 450),
  (6, 3, 2, 900),
  (7, 1, 3, 200),
  (8, 2, 3, 500),
  (9, 3, 3, 200);
