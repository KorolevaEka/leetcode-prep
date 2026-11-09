SELECT test_name, duration_ms FROM test_results WHERE duration_ms >= (SELECT AVG(duration_ms) FROM test_results);
