CREATE DATABASE practiceSQL;
-- DROP DATABASE practiceSQL; 
USE practiceSQL;
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
-- SELECT * FROM staff;
-- ALTER TABLE staff ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
-- ALTER TABLE staff DROP COLUMN is_active;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) NOT NULL;
-- ALTER TABLE staff MODIFY COLUMN email VARCHAR(100) AFTER id;

ALTER TABLE users RENAME COLUMN hire_date TO date_of_birth;
SELECT * FROM users;
