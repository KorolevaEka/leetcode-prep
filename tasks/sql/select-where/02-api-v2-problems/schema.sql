DROP SCHEMA IF EXISTS t CASCADE;
CREATE SCHEMA t;
SET search_path = t;

CREATE TABLE api_requests (api_request_id int PRIMARY KEY, path text, method text, status_code int, latency_ms int);

INSERT INTO api_requests VALUES
  (1, '/api/v2/users', 'GET', 200, 120),
  (2, '/api/v2/users', 'POST', 500, 80),
  (3, '/api/v2/orders', 'GET', 200, 1800),
  (4, '/api/v1/orders', 'GET', 503, 90),
  (5, '/api/v2/orders/42', 'GET', 404, 60),
  (6, '/api/v20/ping', 'GET', 500, 10),
  (7, '/api/v2/search', 'GET', 200, 1500),
  (8, '/api/v2/search', 'GET', 502, 2200),
  (9, '/api/v2/login', 'POST', 200, 300),
  (10, '/health', 'GET', 200, 5000);
