SELECT suite, name, duration_ms FROM (SELECT suite, name, duration_ms, RANK() OVER (ORDER BY duration_ms DESC) AS rnk FROM test_cases) x WHERE rnk <= 2;
