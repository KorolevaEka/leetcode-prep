SELECT suite, name, duration_ms FROM (SELECT suite, name, duration_ms, RANK() OVER (PARTITION BY suite ORDER BY duration_ms DESC) AS rnk FROM test_cases) x WHERE rnk <= 2;
