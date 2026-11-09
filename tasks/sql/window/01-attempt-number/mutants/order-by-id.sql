SELECT test_result_id, ROW_NUMBER() OVER (PARTITION BY test_case_id ORDER BY test_result_id) AS attempt FROM test_results;
