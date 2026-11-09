SELECT r.test_result_id, r.test_run_id FROM test_results r WHERE r.test_run_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM test_runs tr WHERE tr.test_run_id = r.test_result_id);
