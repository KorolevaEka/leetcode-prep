SELECT lower(email) AS email, COUNT(*) AS copies FROM users GROUP BY lower(email) HAVING COUNT(*) > 1;
