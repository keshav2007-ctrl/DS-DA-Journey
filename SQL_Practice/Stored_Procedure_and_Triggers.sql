USE Practicesql;
SELECT * FROM users;
DELIMITER $$
CREATE PROCEDURE select_users()
BEGIN
    SELECT * FROM users;
END $$
CREATE PROCEDURE AddUser(
    IN name  VARCHAR(100),
    IN email VARCHAR(100),
    IN gender ENUM('Male', 'Female', 'other'),
    IN dob DATE,
    IN salary DECIMAL(10, 2)
)
BEGIN
    INSERT INTO users (name, email, gender, date_of_birth, salary) 
    VALUES (name, email, gender, dob, salary);
    SELECT * FROM users;
END $$
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO UserLog (user_id, name, email) 
    VALUES (NEW.id, NEW.name, NEW.email);
END $$
DELIMITER ;
CALL select_users();
CALL AddUser('Johny', 'Johney@example.com', 'Female', '2000-07-21', 75000); --this will insert a new user and also log the action in the UserLog table
SHOW PROCEDURE STATUS WHERE Db = 'Practicesql';   
DROP PROCEDURE IF EXISTS Select_users; --same way a trigger can be dropped using DROP TRIGGER IF EXISTS trigger_name;
SHOW PROCEDURE STATUS WHERE Db = 'Practicesql';   
SELECT * FROM UserLog;
SELECT * FROM users WHERE name LIKE '_A%'; --the no. of underscore defines how many random characters can be there before the letter than we specify.
SELECT DISTINCT gender FROM users;
--truncate table users; --this will delete all the records from the table but the structure of the table will remain intact.
--truncate cannot be rolled back , faster than delete all users 