CREATE DATABASE practiceSQL;
-- DROP DATABASE practiceSQL; 
USE practiceSQL;
<<<<<<< HEAD
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,--primary key can only be one per table and it is used to uniquely identify each record in the table.
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    gender ENUM('Male', 'Female', 'other') NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SELECT * FROM users;
-- RENAME TABLE users TO staff;
=======
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
>>>>>>> 7f1295e ('CRUD_and_Constraints')
-- SELECT * FROM staff;
-- ALTER TABLE staff ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
-- ALTER TABLE staff DROP COLUMN is_active;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) NOT NULL;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) AFTER id;

<<<<<<< HEAD
ALTER TABLE users RENAME COLUMN hire_date TO date_of_birth;
SELECT * FROM users;
=======
ALTER TABLE employees RENAME COLUMN hire_date TO date_of_birth;
SELECT * FROM employees;
>>>>>>> 7f1295e ('CRUD_and_Constraints')
