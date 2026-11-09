SELECT date_trunc('week', executed_at)::date AS week_start, COUNT(*) AS failures FROM test_results GROUP BY 1;
