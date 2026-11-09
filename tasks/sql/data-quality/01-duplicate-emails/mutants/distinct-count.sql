SELECT lower(email) AS email, COUNT(DISTINCT email) AS copies FROM users GROUP BY lower(email) HAVING COUNT(DISTINCT email) > 1;
