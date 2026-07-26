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
SELECT * FROM admin_users;
