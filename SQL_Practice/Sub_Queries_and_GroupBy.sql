USE Practicesql;
SELECT * FROM users;
SELECT * FROM users WHERE referred_by_id IN 
(SELECT id FROM users WHERE   
salary > (SELECT AVG(salary) FROM users));
SELECT name, id, (SELECT AVG(salary) FROM users) AS avg_salary FROM users;
SELECT gender, (SELECT AVG(salary) FROM users) AS avg_salary, COUNT(*) AS user_count 
FROM users WHERE id < 100 
GROUP BY gender WITH ROLLUP HAVING COUNT(*) > 1  ; --rollup gives weighted avg
SELECT referred_by_id, COUNT(*) AS total_referred FROM users
WHERE referred_by_id IS NOT NULL
GROUP BY referred_by_id
HAVING COUNT(*) > 1;
