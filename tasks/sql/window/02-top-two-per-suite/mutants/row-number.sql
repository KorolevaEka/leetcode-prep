SELECT suite, name, duration_ms FROM (SELECT suite, name, duration_ms, ROW_NUMBER() OVER (PARTITION BY suite ORDER BY duration_ms DESC, name) AS rnk FROM test_cases) x WHERE rnk <= 2;
