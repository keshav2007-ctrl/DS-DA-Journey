USE PracticeSQL;
SELECT * FROM employees;
SELECT * FROM adresses;
SELECT employees.first_name, adresses.street, employees.salary, adresses.city, adresses.id
FROM employees
INNER JOIN adresses on  employees.id = adresses.employees_id;
SELECT employees.first_name, adresses.street
FROM employees
LEFT JOIN adresses ON employees.id = adresses.employees_id;
SELECT employees.*, adresses.*
FROM employees
RIGHT JOIN adresses ON employees.id = adresses.employees_id;--adresses.id will return null 
