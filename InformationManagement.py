import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def createMainWindow():
    root = tk.Tk()
    root.title("Created by: John Lemar Gonzales")

    appLabel = tk.Label(root, text="USTP Student Information System", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

    firstNameLabel = tk.Label(root, text="Enter Your First Name:", width=40, anchor='w', font=("Sylfaen", 12))
    firstNameLabel.grid(row=1, column=0, padx=(10,0), pady=(30, 0))
    lastNameLabel = tk.Label(root, text="Enter Your Last Name:", width=40, anchor='w', font=("Sylfaen", 12))
    lastNameLabel.grid(row=2, column=0, padx=(10,0))
    courseLabel = tk.Label(root, text="Enter Your Course:", width=40, anchor='w', font=("Sylfaen", 12))
    courseLabel.grid(row=3, column=0, padx=(10,0))
    yearLevelLabel = tk.Label(root, text="Enter Your Year Level:", width=40, anchor='w', font=("Sylfaen", 12))
    yearLevelLabel.grid(row=4, column=0, padx=(10,0))
    studentIdLabel = tk.Label(root, text="Enter Your Student ID:", width=40, anchor='w', font=("Sylfaen", 12))
    studentIdLabel.grid(row=5, column=0, padx=(10,0))
    phoneNumberLabel = tk.Label(root, text="Enter Your Phone Number:", width=40, anchor='w', font=("Sylfaen", 12))
    phoneNumberLabel.grid(row=6, column=0, padx=(10,0))

    firstNameEntry = tk.Entry(root, width=30)
    lastNameEntry = tk.Entry(root, width=30)
    courseEntry = tk.Entry(root, width=30)
    yearLevelEntry = tk.Entry(root, width=30)
    studentIdEntry = tk.Entry(root, width=30)
    phoneNumberEntry = tk.Entry(root, width=30)

    firstNameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    lastNameEntry.grid(row=2, column=1, padx=(0,10), pady=20)
    courseEntry.grid(row=3, column=1, padx=(0,10), pady=20)
    yearLevelEntry.grid(row=4, column=1, padx=(0,10), pady=20)
    studentIdEntry.grid(row=5, column=1, padx=(0,10), pady=20)
    phoneNumberEntry.grid(row=6, column=1, padx=(0,10), pady=20)

    button = tk.Button(root, text="Save Information", command=lambda: takeNameInput(root, firstNameEntry, lastNameEntry, courseEntry, yearLevelEntry, studentIdEntry, phoneNumberEntry))
    button.grid(row=7, column=0, pady=30)

    displayButton = tk.Button(root, text="Display All Information", command=lambda: displayResults(root))
    displayButton.grid(row=7, column=1)

    root.mainloop()

def takeNameInput(root, firstNameEntry, lastNameEntry, courseEntry, yearLevelEntry, studentIdEntry, phoneNumberEntry):
    firstName = firstNameEntry.get()
    firstNameEntry.delete(0, tk.END)
    lastName = lastNameEntry.get()
    lastNameEntry.delete(0, tk.END)
    course = courseEntry.get()
    courseEntry.delete(0, tk.END)
    yearLevel = yearLevelEntry.get()
    yearLevelEntry.delete(0, tk.END)
    studentId = studentIdEntry.get()
    studentIdEntry.delete(0, tk.END)
    phoneNumber = phoneNumberEntry.get()
    phoneNumberEntry.delete(0, tk.END)

    try:
        cursor.execute(f"INSERT INTO {TABLE_NAME} (First_Name, Last_Name, Course, Year_Level, StudentID, Phone_Number) VALUES (%s, %s, %s, %s, %s, %s)", (firstName, lastName, course, yearLevel, studentId, phoneNumber))
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def displayResults(root):
    secondWindow = tk.Toplevel(root)
    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five", "six")

    tree.heading("one", text="First Name")
    tree.heading("two", text="Last Name")
    tree.heading("three", text="Course")
    tree.heading("four", text="Year Level")
    tree.heading("five", text="Student ID")
    tree.heading("six", text="Phone Number")

    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        i = 0
        for row in cursor.fetchall():
            tree.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

    tree.pack()

    backButton = tk.Button(secondWindow, text="Back", command=secondWindow.destroy)
    backButton.pack()

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="HelloWorld0429!",
        database="student_management"
    )

    cursor = connection.cursor()

    TABLE_NAME = "students"

    createMainWindow()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
