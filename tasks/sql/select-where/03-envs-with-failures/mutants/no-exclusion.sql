SELECT DISTINCT lower(env) AS env FROM test_runs WHERE status = 'failed' AND started_at >= '2024-03-01' AND started_at < '2024-03-08';
