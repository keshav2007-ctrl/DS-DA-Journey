USE practiceSQL;

SELECT * FROM employees;
SELECT COUNT(*) AS total_employees, MIN(salary) AS minimum_salary, MAX(salary) AS maximum_salary FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT gender, SUM(salary) AS total_salary FROM employees GROUP BY gender;

SELECT gender, UPPER(first_name) AS upper_name, CONCAT(first_name, 'DA26') AS username, LENGTH(first_name) AS name_length FROM employees;
SELECT first_name, last_name, CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

SELECT first_name, FLOOR(DATEDIFF(CURDATE(), date_of_birth)/365.25) AS age_in_years FROM employees;
SELECT salary,
    ROUND(salary),
    FLOOR(salary),
    CEIL(salary) FROM employees;
SELECT first_name, gender,
    if(gender = 'MALE', 'Yes', 'No') AS is_male FROM employees;
