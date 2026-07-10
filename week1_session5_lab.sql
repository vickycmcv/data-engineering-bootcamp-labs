-- Understanding the Data
-- 1. Display all employees.
SELECT * FROM Employees
-- 2. Display only the employee names and salaries.
SELECT FirstName, Salary FROM Employees
-- 3. Count the total number of employees.
SELECT COUNT(*) FROM Employees
-- 4. Display all unique cities.
SELECT DISTINCT(City) FROM Employees
-- 5. Display all unique department IDs.
SELECT DISTINCT(DepartmentID) FROM Employees

--Filtering
-- 6. Find employees older than 30.
SELECT * FROM Employees WHERE Age > 30
-- 7. Find employees earning more than 60,000.
SELECT * FROM Employees WHERE Salary > 60000
-- 8. Display employees from London.
SELECT * FROM Employees WHERE City = "London"
-- 9. Find employees whose salary is between 50,000 and 75,000.
SELECT * FROM Employees WHERE Salary BETWEEN 50000 AND 75000
-- 10. Display employees whose first name starts with L.
SELECT * FROM Employees WHERE FirstName like "L%"
-- 11. Display employees whose age is less than 35.
SELECT * FROM Employees WHERE Age < 35

-- Sorting
-- 12. Sort employees by salary (highest first).
SELECT * FROM Employees ORDER BY Salary DESC
-- 13. Sort employees by age (youngest first).
SELECT * FROM Employees ORDER BY Age 
-- 14. Sort employees by city and then salary.
SELECT * FROM Employees ORDER BY City ASC, Salary DESC

-- Aggregate Functions
-- 15. Find the average salary.
SELECT avg(Salary) AS avg_salaty FROM Employees
-- 16. Find the highest salary.
SELECT max(Salary) AS highest_salary FROM Employees
-- 17. Find the minimum salary.
SELECT min(Salary) AS min_salary FROM Employees
-- 18. Find the average employee age.
SELECT avg(Age) AS avg_age FROM Employees

-- GROUP BY
-- 19. Count employees in each department.
SELECT DepartmentID, count(*) AS total_employees FROM Employees GROUP BY DepartmentID
-- 20. Find the average salary in each department.
SELECT DepartmentID, avg(Salary) AS avg_salaty FROM Employees GROUP BY DepartmentID
-- 21. Find the highest salary in each department.
SELECT DepartmentID, max(Salary) AS highest_salary FROM Employees GROUP BY DepartmentID
-- 22. Show only departments having more than one employee.
SELECT DepartmentID, count(*) AS total_employees FROM Employees GROUP BY DepartmentID HAVING total_employees > 1

-- UPDATE
-- 23. Increase salaries of IT employees by 5%.
UPDATE Employees SET Salary = Salary*1.05 WHERE DepartmentID = 3;
-- 24. Change the city of EmployeeID 109 to Brussels.
UPDATE Employees SET City = "Brussels" WHERE EmployeeID = 109;

-- DELETE
-- 25. Delete employees whose salary is below 48,000.
DELETE FROM Employees WHERE Salary < 48000;

-- JOIN Exercises
-- 26. Display each employee along with their department name.
SELECT
	e.*,
	d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
-- 27. Display employee name, department name, and department location.
SELECT
	e.FirstName,
	d.DepartmentName,
	d.Location
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
-- 28. Count the number of employees in each department using a JOIN.
SELECT
	d.DepartmentName,
	count(*) AS total_employees
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
GROUP BY d.DepartmentName
-- 29. Display all departments, even if they have no employees.
SELECT
	d.DepartmentName,
	count(*) AS total_employees
FROM Departments d
LEFT JOIN Employees e ON d.DepartmentID=e.DepartmentID
GROUP BY d.DepartmentName
-- 30. Find the average salary for each department using a JOIN.
SELECT
	d.DepartmentName,
	avg(e.Salary) AS AVG_Salary
FROM Departments d
LEFT JOIN Employees e ON d.DepartmentID=e.DepartmentID
GROUP BY d.DepartmentName
-- 31. Display employees who work in departments located in Berlin.
SELECT
	e.*,
	d.Location as DepartmentLocation
FROM Departments d
LEFT JOIN Employees e ON d.DepartmentID=e.DepartmentID
WHERE d.Location = "Berlin"
-- 32. Display only employees working in the IT department (using a JOIN instead of filtering by ID).
SELECT
	e.*,
	d.DepartmentName
FROM Departments d
LEFT JOIN Employees e ON d.DepartmentID=e.DepartmentID
WHERE d.DepartmentName = "IT"

-- Bonus Challenges
-- 33. Display the Top 3 highest-paid employees.
SELECT * FROM Employees ORDER BY Salary DESC LIMIT 3
-- 34. Find employees whose salary is above the company average.
SELECT * FROM Employees WHERE Salary > (SELECT avg(Salary) FROM Employees)
-- 35. Find the department with the highest average salary.
SELECT
	d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
GROUP BY d.DepartmentName
HAVING AVG(E.SALARY)
ORDER BY AVG(E.SALARY) DESC
LIMIT 1
-- 36. Display the oldest employee in each department.
SELECT
	d.DepartmentName,
	e.*
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
GROUP BY d.DepartmentName
HAVING max(E.AGE)
-- 37. Display employees whose last name contains the letter 'o'.
SELECT * FROM Employees WHERE LastName like "%o%"
-- 38. Show the total salary paid by each department.
SELECT
	d.DepartmentName,
	SUM(e.Salary) AS TotalSalary
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID=d.DepartmentID
GROUP BY d.DepartmentName
-- 39. Display employees earning the second-highest salary.
WITH ranked_salary as(
	SELECT
		*,
		RANK()OVER (ORDER BY Salary DESC) AS SalaryRank
FROM Employees 
)

SELECT * FROM ranked_salary WHERE SalaryRank = 2

-- 40. Find the city with the highest number of employees.
WITH employees_by_city AS (
	SELECT City, COUNT(*) AS EmployeeCount
    FROM Employees
    GROUP BY City
)
SELECT
	City,
	EmployeeCount
FROM employees_by_city
WHERE (SELECT max(EmployeeCount) AS MaxNumEmployees FROM employees_by_city)

-- Other way to do it
WITH ranked_salary as(
	SELECT
		City,
		COUNT(*) AS EmployeeCount,
		RANK()OVER (ORDER BY count(*) DESC) AS SalaryRank
FROM Employees
group by city
)

SELECT City FROM ranked_salary WHERE SalaryRank = 1
