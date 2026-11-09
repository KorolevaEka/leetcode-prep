SELECT c.name FROM test_cases c LEFT JOIN test_results r ON r.test_case_id = c.test_case_id WHERE r.test_result_id = NULL;
