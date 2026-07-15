CREATE DATABASE practiceSQL;
-- DROP DATABASE practiceSQL; 
USE practiceSQL;
CREATE TABLE employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    gender ENUM('Male', 'Female', 'other') NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
)
-- SELECT * FROM employees;
-- RENAME TABLE employees TO staff;
-- SELECT * FROM staff;
-- ALTER TABLE staff ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
-- ALTER TABLE staff DROP COLUMN is_active;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) NOT NULL;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) AFTER id;

ALTER TABLE employees RENAME COLUMN hire_date TO date_of_birth;
SELECT * FROM employees;
