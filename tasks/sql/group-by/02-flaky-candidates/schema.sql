DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE test_cases (test_case_id int PRIMARY KEY, name text);
CREATE TABLE test_results (test_result_id int PRIMARY KEY, test_case_id int REFERENCES test_cases, status text);

INSERT INTO test_cases VALUES
  (1, 'login'),
  (2, 'checkout'),
  (3, 'search'),
  (4, 'export'),
  (5, 'profile'),
  (6, 'reports');
INSERT INTO test_results VALUES
  (1, 1, 'passed'),
  (2, 1, 'failed'),
  (3, 1, 'passed'),
  (4, 1, 'passed'),
  (5, 1, 'passed'),
  (6, 1, 'passed'),
  (7, 1, 'failed'),
  (8, 1, 'passed'),
  (9, 2, 'passed'),
  (10, 2, 'failed'),
  (11, 2, 'passed'),
  (12, 2, 'failed'),
  (13, 3, 'passed'),
  (14, 3, 'passed'),
  (15, 3, 'failed'),
  (16, 3, 'passed'),
  (17, 3, 'failed'),
  (18, 4, 'failed'),
  (19, 4, 'failed'),
  (20, 4, 'failed'),
  (21, 5, 'passed'),
  (22, 5, 'passed'),
  (23, 5, 'passed'),
  (24, 5, 'passed'),
  (25, 5, 'passed'),
  (26, 5, 'passed'),
  (27, 6, 'passed'),
  (28, 6, 'passed'),
  (29, 6, 'passed'),
  (30, 6, 'failed'),
  (31, 6, 'passed'),
  (32, 6, 'passed'),
  (33, 6, 'passed'),
  (34, 6, 'passed');
