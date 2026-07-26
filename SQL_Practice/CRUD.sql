USE practiceSQL;

SELECT * FROM users ORDER BY salary DESC;
SELECT * FROM users WHERE salary > 60000;
SELECT * FROM users WHERE salary BETWEEN 50000 AND 70000;

UPDATE users SET salary = salary * 1.1 WHERE date_of_birth < '2020-01-01';
UPDATE users SET salary = salary+10000 WHERE salary<60000;
DELETE FROM users WHERE date_of_birth < '1990-01-01';
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);
ALTER TABLE users ADD CONSTRAINT check_dob CHECK (date_of_birth > '1990-01-01');
-- INSERT INTO users (first_name, last_name, email, date_of_birth, salary) VALUES
-- ('john', 'foe', 'asd@example.com', '1989-01-01', 50000);
SELECT * FROM users;