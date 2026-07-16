USE practiceSQL;
SELECT*FROM employees;
COMMIT;
SET AUTOCOMMIT = 0; 
--now we can make multiple changes to the database and 
--if any mistakes were made we can use ROLLBACK to the last time we used COMMIT; undoing all the changes made.
--FOR EXAMPLE:
--DELETE FROM employees WHERE employee_id = 1; this is the query we wanted to run but by mistake we ran it for id=2.
DELETE FROM employees WHERE employee_id = 2;
--ROLLBACK; can help us in rectifying this mistake and delete the actual employee we wanted to delete.
ROLLBACK;
--SET AUTOCOMMIT = 1; turns on autocommit again.

