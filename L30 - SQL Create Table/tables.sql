CREATE TABLE IF NOT EXISTS STUDENTS(
    NAME TEXT,
    ID_NO INTEGER,
    GRADE VARCHAR(20)
);

INSERT INTO STUDENTS VALUES
("Mary", 2021, "12"),
("Moses", 2020, "11"),
("Martin", 2019, "12"),
("Mubarak", 2018, "10"),
("Musa", 2017, "12"),
("Micheal", 2016, "11");

SELECT * FROM STUDENTS;

CREATE TABLE IF NOT EXISTS salesman(
    salesman_id INT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission REAL
);

INSERT INTO salesman VALUES
(101, "James", "New York", 10),
(105, "Julian", "Canada", 15),
(103, "Jacob", "Los Angeles", 13),
(102, "Joseph", "Nigeria", 11);

SELECT * FROM salesman;
SELECT name,city FROM salesman;

