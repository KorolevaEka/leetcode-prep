SELECT test_result_id, ROW_NUMBER() OVER (ORDER BY executed_at) AS attempt FROM test_results;
