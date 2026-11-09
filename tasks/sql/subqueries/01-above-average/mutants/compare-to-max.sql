SELECT test_name, duration_ms FROM test_results WHERE duration_ms > (SELECT MAX(duration_ms) FROM test_results);
