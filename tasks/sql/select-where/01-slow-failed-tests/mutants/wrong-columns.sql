SELECT suite, duration_ms FROM test_results WHERE status = 'failed' AND duration_ms > 2000;
