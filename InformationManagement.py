import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def createMainWindow():
    root = tk.Tk()
    root.title("Created by: John Lemar Gonzales")

    appLabel = tk.Label(root, text="Student Information System", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

    nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                         font=("Sylfaen", 12))
    nameLabel.grid(row=1, column=0, padx=(10,0), pady=(30, 0))
    collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                            font=("Sylfaen", 12))
    collegeLabel.grid(row=2, column=0, padx=(10,0))
    phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                          font=("Sylfaen", 12))
    phoneLabel.grid(row=3, column=0, padx=(10,0))
    courseLabel = tk.Label(root, text="Enter your course", width=40, anchor='w',
                            font=("Sylfaen", 12))
    courseLabel.grid(row=4, column=0, padx=(10,0))

    nameEntry = tk.Entry(root, width=30)
    collegeEntry = tk.Entry(root, width=30)
    phoneEntry = tk.Entry(root, width=30)
    courseEntry = tk.Entry(root, width=30)

    nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    collegeEntry.grid(row=2, column=1, padx=(0,10), pady=20)
    phoneEntry.grid(row=3, column=1, padx=(0,10), pady=20)
    courseEntry.grid(row=4, column=1, padx=(0,10), pady=20)

    button = tk.Button(root, text="Save Information", command=lambda: takeNameInput(root, nameEntry, collegeEntry, phoneEntry, courseEntry))
    button.grid(row=5, column=0, pady=30)

    displayButton = tk.Button(root, text="Display All Information", command=lambda: displayResults(root))
    displayButton.grid(row=5, column=1)

    root.mainloop()

def takeNameInput(root, nameEntry, collegeEntry, phoneEntry, courseEntry):
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get().upper()  # Convert to uppercase
    collegeEntry.delete(0, tk.END)
    phone = phoneEntry.get()
    phoneEntry.delete(0, tk.END)
    course = courseEntry.get().upper()  # Convert to uppercase
    courseEntry.delete(0, tk.END)

    try:
        cursor.execute(f"INSERT INTO {TABLE_NAME} ({STUDENT_NAME}, {STUDENT_COLLEGE}, {STUDENT_COURSE}, {STUDENT_PHONE}) VALUES (%s, %s, %s, %s)", (username, collegeName, course, phone))
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def displayResults(root):
    secondWindow = tk.Toplevel(root)
    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Course")
    tree.heading("four", text="Phone Number")

    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        i = 0
        for row in cursor.fetchall():
            tree.insert('', i, text="Student " + str(row[0]),
                        values=(row[1], row[2], row[3], row[4]))
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
    STUDENT_ID = "student_id"
    STUDENT_NAME = "student_name"
    STUDENT_COLLEGE = "student_college"
    STUDENT_COURSE = "course"
    STUDENT_PHONE = "student_phone"

    createMainWindow()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
