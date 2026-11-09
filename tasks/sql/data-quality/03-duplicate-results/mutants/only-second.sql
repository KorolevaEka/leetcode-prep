SELECT test_result_id FROM (SELECT test_result_id, ROW_NUMBER() OVER (PARTITION BY test_run_id, test_case_id ORDER BY test_result_id) AS rn FROM test_results) x WHERE rn = 2;
