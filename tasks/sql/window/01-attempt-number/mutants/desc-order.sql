SELECT test_result_id, ROW_NUMBER() OVER (PARTITION BY test_case_id ORDER BY executed_at DESC) AS attempt FROM test_results;
