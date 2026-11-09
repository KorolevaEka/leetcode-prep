SELECT r.test_result_id, r.test_run_id FROM test_results r LEFT JOIN test_runs tr ON tr.test_run_id = r.test_run_id WHERE tr.test_run_id IS NULL;
