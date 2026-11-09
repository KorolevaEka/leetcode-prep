SELECT DISTINCT lower(env) AS env FROM test_runs WHERE status = 'failed' AND started_at BETWEEN '2024-03-01' AND '2024-03-07' AND lower(env) NOT IN ('local', 'dev');
