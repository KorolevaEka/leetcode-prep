SELECT p.last_name, p.first_name, a.city, a.state
FROM person p
LEFT JOIN address a ON a.person_id = p.person_id;
