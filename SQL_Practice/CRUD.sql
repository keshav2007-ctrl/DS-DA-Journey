USE practiceSQL;

SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees WHERE salary > 60000;
SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000;

UPDATE employees SET salary = salary * 1.1 WHERE date_of_birth < '2020-01-01';
UPDATE employees SET salary = salary+10000 WHERE salary<60000;
DELETE FROM employees WHERE date_of_birth < '1990-01-01';
ALTER TABLE employees ADD CONSTRAINT unique_email UNIQUE (email);
ALTER TABLE employees ADD CONSTRAINT check_dob CHECK (date_of_birth > '1990-01-01');
-- INSERT INTO employees (first_name, last_name, email, date_of_birth, salary) VALUES
-- ('john', 'foe', 'asd@example.com', '1989-01-01', 50000);
SELECT * FROM employees;