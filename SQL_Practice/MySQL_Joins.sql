USE PracticeSQL;
SELECT * FROM users;
SELECT * FROM addresses;
SELECT users.first_name, addresses.street, users.salary, addresses.city, addresses.id
FROM users
INNER JOIN addresses on  users.id = addresses.users_id;
SELECT users.first_name, addresses.street
FROM users
LEFT JOIN addresses ON users.id = addresses.users_id;
SELECT users.*, addresses.*
FROM users
RIGHT JOIN addresses ON users.id = addresses.users_id;--addresses.id will return null 
SELECT * FROM users
UNION
SELECT name, email, date_of_birth, 'ADMIN' AS role FROM admin_users
ORDER BY date_of_birth;
ALTER TABLE users ADD COLUMN referred_by_id INT;
UPDATE users SET referred_by_id = 1 WHERE id IN (2, 3, 13, 15, 19 ,25);
UPDATE users SET referred_by_id = 5 WHERE id = 4;
SELECT
a.id,
a.name AS user_name,
b.name AS referred_by_name
FROM users a
INNER JOIN users b ON a.referred_by_id = b.id;
CREATE VIEW rich_users AS
SELECT * FROM users WHERE salary > 68000;
SELECT * FROM rich_users ORDER BY salary DESC;
UPDATE users SET salary = 75000 WHERE id = 1;
SELECT * FROM rich_users ORDER BY salary DESC;
ALTER VIEW rich_users AS
SELECT * FROM users WHERE salary > 80000;
SELECT * FROM rich_users ORDER BY salary DESC;
SHOW INDEXES FROM users;
ALTER TABLE users DROP INDEX email;
