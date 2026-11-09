SELECT r.test_result_id, r.test_run_id FROM test_results r JOIN test_runs tr ON tr.test_run_id = r.test_run_id;
