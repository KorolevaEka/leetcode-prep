SELECT api_request_id, path, status_code, latency_ms FROM api_requests WHERE path LIKE '/api/v2/%' AND (status_code >= 500 OR latency_ms >= 1500);
