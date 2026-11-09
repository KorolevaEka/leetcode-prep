DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE defects (defect_id int PRIMARY KEY, title text, severity text, opened_at timestamp, closed_at timestamp);

INSERT INTO defects VALUES
  (1, 'Login 500', 'critical', '2024-03-01 08:00', '2024-03-02 08:00'),
  (2, 'Cart total wrong', 'critical', '2024-03-05 10:00', '2024-03-07 10:00'),
  (3, 'Export hangs', 'critical', '2024-03-10 09:00', '2024-03-14 09:00'),
  (4, 'Payment timeout', 'critical', '2024-03-30 12:00', NULL),
  (5, 'Session leak', 'critical', '2024-03-20 08:00', NULL),
  (6, 'Wrong locale', 'major', '2024-03-02 09:30', '2024-03-03 21:30'),
  (7, 'Search lag', 'major', '2024-03-04 12:00', '2024-03-09 12:00'),
  (8, 'Broken filter', 'major', '2024-03-15 00:00', NULL),
  (9, 'Typo on form', 'minor', '2024-03-12 14:00', '2024-03-12 18:30');
