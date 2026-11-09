SELECT EXTRACT(week FROM executed_at) AS week_start, COUNT(*) AS failures FROM test_results WHERE status = 'failed' GROUP BY 1;
