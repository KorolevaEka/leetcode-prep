SELECT suite, COUNT(*) AS executed, ROUND(100.0 * COUNT(*) FILTER (WHERE status = 'passed') / NULLIF(COUNT(*), 0), 1) AS pass_rate FROM test_results GROUP BY suite;
