SELECT email, COUNT(*) AS copies FROM users GROUP BY email HAVING COUNT(*) > 1;
