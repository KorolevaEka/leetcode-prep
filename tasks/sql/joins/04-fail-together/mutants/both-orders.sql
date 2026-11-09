SELECT a.name AS name_a, b.name AS name_b, COUNT(*) AS runs_together
FROM test_results ra
JOIN test_results rb ON rb.test_run_id = ra.test_run_id AND rb.test_case_id <> ra.test_case_id AND rb.status = 'failed'
JOIN test_cases a ON a.test_case_id = ra.test_case_id
JOIN test_cases b ON b.test_case_id = rb.test_case_id
WHERE ra.status = 'failed'
GROUP BY a.name, b.name
HAVING COUNT(*) >= 2;
