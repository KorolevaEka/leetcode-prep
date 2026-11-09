SELECT c.name FROM test_cases c JOIN test_results r ON r.test_case_id = c.test_case_id WHERE r.test_result_id IS NULL;
