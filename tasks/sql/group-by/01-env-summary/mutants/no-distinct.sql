SELECT env, COUNT(*) AS results, COUNT(test_case_id) AS distinct_cases, MAX(duration_ms) AS slowest_ms FROM test_results GROUP BY env;
