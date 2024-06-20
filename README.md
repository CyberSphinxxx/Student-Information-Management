# USTP Student Information System
```Created By: John Lemar L. Gonzales, BSIT1-R10```

---------------------------------------------------
**Flowchart**
You can access the flowchart through this link:

https://lucid.app/lucidchart/cdc3c188-ac4c-47f9-a381-3632e41f4f14/edit?viewport_loc=-567%2C-622%2C2631%2C1770%2C0_0&invitationId=inv_8d79eed1-02b5-4a45-a729-d0a2a45b612d

---------------------------------------------------
**DOCS**
You can access the Google DOCS Documentation through this link:

https://docs.google.com/document/d/13sB8g_PUSqZbxPcvjDIym-SkQOuCh7IPwO3_KbSQe00/edit?usp=sharing

---------------------------------------------------
**USTP Student Information System Description:**

This repository contains a simple Student Information System implemented using Python's Tkinter library for the GUI and MySQL for the database. It allows users to input their personal information such as first name, last name, course, year level, student ID, and phone number, and save it to a MySQL database.

---------------------------------------------------
**User Input Prompt:**

The program provides fields for the user to input their personal information.

---------------------------------------------------
**Data Saving:**

After receiving the input data, the program saves it to a MySQL database.

---------------------------------------------------
**Display All Information:**

The program allows users to display all information saved in the database.

---------------------------------------------------
**Usage:**

1. Make sure your MySQL server is running.
2. Run the application using the provided Python script.
3. Enter the required information in the GUI window.
4. Click on the "Save Information" button to save the data.
5. To display all information saved in the database, click on the "Display All Information" button.

---------------------------------------------------
# Python code for the main application (main.py)
```
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

#The Python code goes here
```
---------------------------------------------------
# MySQL database schema
```
CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Course VARCHAR(255) NOT NULL,
    Year_Level VARCHAR(255) NOT NULL,
    StudentID VARCHAR(255) NOT NULL,
```
---------------------------------------------------
# Notes:

- Make sure to replace ```your-username``` with your actual GitHub/SQL username.
- Modify the MySQL connection parameters in main.py to match your MySQL setup.
- This README assumes basic familiarity with Git, Python, Tkinter, and MySQL.
- Before running the application, ensure that your **MySQL server** is running and accessible.
- Contributions to improve the system are highly encouraged and appreciated.
- This project is provided under the MIT License, granting open-source usage with proper attribution.
- Special thanks to the developers of Tkinter and MySQL Connector/Python for their excellent documentation.
