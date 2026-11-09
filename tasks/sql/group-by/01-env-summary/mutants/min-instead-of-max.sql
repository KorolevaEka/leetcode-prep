SELECT env, COUNT(*) AS results, COUNT(DISTINCT test_case_id) AS distinct_cases, MIN(duration_ms) AS slowest_ms FROM test_results GROUP BY env;
