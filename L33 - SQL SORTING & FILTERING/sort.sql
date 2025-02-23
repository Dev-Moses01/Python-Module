CREATE TABLE IF NOT EXISTS DEPARTMENT(
    NAME TEXT,
    ID INT PRIMARY KEY,
    GENDER TEXT,
    DEPT_NAME TEXT,
    SALARY INT
);

INSERT INTO DEPARTMENT VALUES
('Moses', 1, 'Male', 'Big data', 100000),
('Mark', 4, 'Male', 'AI', 15000),
('Mary', 2, 'Female','Marketing', 78000),
('Matthew', 5, 'Male', 'IT', 20000),
('Scott', 3, 'Male', 'AI', 40000),
('Aurora', 8, 'Female', 'Big data', 80000),
('Joseph', 7, 'Male', 'IT', 25000),
('Kate', 10, 'Female', 'Marketing', 70000);

SELECT * FROM DEPARTMENT;

SELECT DISTINCT GENDER FROM DEPARTMENT;

--what your selecting is what you are grouping by
SELECT GENDER, MAX(SALARY), MIN(SALARY), AVG(SALARY)
FROM DEPARTMENT
GROUP BY GENDER;

SELECT DEPT_NAME, AVG(SALARY)
FROM DEPARTMENT
GROUP BY DEPT_NAME;

SELECT GENDER, COUNT(GENDER) FROM DEPARTMENT
GROUP BY GENDER;
SELECT DEPT_NAME, COUNT(NAME) FROM DEPARTMENT
GROUP BY DEPT_NAME;

--SORT
SELECT * FROM DEPARTMENT
ORDER BY GENDER,  SALARY;
--DESC FOR DESCENDING

SELECT ID, DEPT_NAME FROM DEPARTMENT
ORDER BY DEPT_NAME, ID DESC;