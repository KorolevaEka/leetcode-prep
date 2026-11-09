SELECT tr.env, b.version, r.test_name FROM test_results r JOIN test_runs tr ON tr.test_run_id = r.test_run_id JOIN builds b ON b.build_id = tr.build_id WHERE r.status = 'failed';
