CREATE DATABASE IF NOT EXISTS student_management;

USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Course VARCHAR(255) NOT NULL,
    Year_Level VARCHAR(50) NOT NULL,
    StudentID VARCHAR(50) NOT NULL,
    Phone_Number VARCHAR(15) NOT NULL
);

SELECT * FROM students;
