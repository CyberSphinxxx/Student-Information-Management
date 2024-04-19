import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def displayResults(root, cursor, TABLE_NAME):
    def refresh():
        tree.delete(*tree.get_children())
        try:
            cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            i = 0
            for row in cursor.fetchall():
                tree.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
                i += 1
            update_total_students_label(total_students_label)  # Update total students counter
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def update_total_students_label(label):
        total_students = len(tree.get_children())
        label.config(text=f"Total Students: {total_students}")

    def search():
        selected_criteria = searchCriteria.get()
        keyword = searchKeyword.get()

        if selected_criteria and keyword:
            searchDatabase(selected_criteria, keyword, tree, TABLE_NAME)  # Pass TABLE_NAME argument here
        else:
            messagebox.showwarning("Warning", "Please select a search criteria and enter a keyword.")

    secondWindow = tk.Toplevel(root)
    secondWindow.title("Display Results")

    appLabel = tk.Label(secondWindow, text="USTP Student Management System", fg="#06a099")
    appLabel.config(font=("Arial", 24, "bold"))
    appLabel.pack(pady=(20, 10))

    searchFrame = tk.Frame(secondWindow)
    searchFrame.pack(pady=(0, 10), padx=10, fill="x")

    searchCriteriaLabel = tk.Label(searchFrame, text="Search by:", font=("Arial", 12))
    searchCriteriaLabel.grid(row=0, column=0, padx=5, pady=5)

    searchCriteria = ttk.Combobox(searchFrame, values=("First Name", "Last Name", "Course", "Year Level", "Student ID"), font=("Arial", 12))
    searchCriteria.grid(row=0, column=1, padx=5, pady=5)
    searchCriteria.set("First Name")  # Default selection

    searchKeywordLabel = tk.Label(searchFrame, text="Keyword:", font=("Arial", 12))
    searchKeywordLabel.grid(row=0, column=2, padx=5, pady=5)

    searchKeyword = tk.Entry(searchFrame, font=("Arial", 12))
    searchKeyword.grid(row=0, column=3, padx=5, pady=5)

    searchButton = tk.Button(searchFrame, text="Search", font=("Arial", 12), command=search)
    searchButton.grid(row=0, column=4, padx=5, pady=5)

    refreshButton = tk.Button(searchFrame, text="Refresh", font=("Arial", 12), command=refresh)
    refreshButton.grid(row=0, column=5, padx=5, pady=5)

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
        total_students_label = tk.Label(secondWindow, text="Total Students: ", font=("Arial", 12))
        total_students_label.pack(pady=(10, 0))
        update_total_students_label(total_students_label)  # Update total students counter
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

    tree.pack(expand=True, fill="both")

    backButton = tk.Button(secondWindow, text="Back", font=("Arial", 12), command=secondWindow.destroy)
    backButton.pack(pady=(10, 20))

def createMainWindow(cursor, TABLE_NAME):
    def takeNameInput(*entries):
        data = [entry.get() for entry in entries]
        if all(data):
            try:
                cursor.execute(f"INSERT INTO {TABLE_NAME} (First_Name, Last_Name, Course, Year_Level, StudentID, Phone_Number) VALUES (%s, %s, %s, %s, %s, %s)", tuple(data))
                connection.commit()
                messagebox.showinfo("Success", "Data Saved Successfully.")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error occurred: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please fill all the necessary information to proceed.")

    root = tk.Tk()
    root.title("Created by: John Lemar Gonzales")

    appLabel = tk.Label(root, text="USTP Student Information System", fg="#06a099")
    appLabel.config(font=("Arial", 24, "bold"))
    appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0), sticky="ew")

    labels = ["First Name:", "Last Name:", "Course:", "Year Level:", "Student ID:", "Phone Number:"]
    entries = []

    for idx, label_text in enumerate(labels):
        label = tk.Label(root, text=label_text, font=("Arial", 12))
        label.grid(row=idx + 1, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        entry = tk.Entry(root, font=("Arial", 12))
        entry.grid(row=idx + 1, column=1, padx=(0, 10), pady=(10, 0), sticky="ew")
        entries.append(entry)

    button = tk.Button(root, text="Save Information", font=("Arial", 12), command=lambda: takeNameInput(*entries))
    button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=30)

    displayButton = tk.Button(root, text="Display All Information", font=("Arial", 12), command=lambda: loginWindow(root, cursor, TABLE_NAME))
    displayButton.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

    for i in range(len(labels) + 3):
        root.grid_rowconfigure(i, weight=1)

    for i in range(2):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

def loginWindow(root, cursor, TABLE_NAME):
    loginWindow = tk.Toplevel(root)
    loginWindow.title("Login")

    usernameLabel = tk.Label(loginWindow, text="Username:", font=("Arial", 12))
    usernameLabel.grid(row=0, column=0, padx=5, pady=5)
    usernameEntry = tk.Entry(loginWindow, font=("Arial", 12))
    usernameEntry.grid(row=0, column=1, padx=5, pady=5)

    passwordLabel = tk.Label(loginWindow, text="Password:", font=("Arial", 12))
    passwordLabel.grid(row=1, column=0, padx=5, pady=5)
    passwordEntry = tk.Entry(loginWindow, show="*", font=("Arial", 12))
    passwordEntry.grid(row=1, column=1, padx=5, pady=5)

    loginButton = tk.Button(loginWindow, text="Login", font=("Arial", 12), command=lambda: authenticate(usernameEntry.get(), passwordEntry.get(), loginWindow, root, cursor, TABLE_NAME))
    loginButton.grid(row=2, columnspan=2, padx=5, pady=5)

def authenticate(username, password, loginWindow, root, cursor, TABLE_NAME):
    if username == "admin" and password == "admin123":
        loginWindow.destroy()
        displayResults(root, cursor, TABLE_NAME)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def searchDatabase(selected_criteria, keyword, tree, TABLE_NAME):
    for row in tree.get_children():
        tree.delete(row)

    try:
        sql = f"SELECT * FROM {TABLE_NAME} WHERE "
        if selected_criteria == "Year_Level" or selected_criteria == "Student ID":
            sql += f"`{selected_criteria}` = %s"
            cursor.execute(sql, (keyword,))
        else:
            sql += f"`{selected_criteria.replace(' ', '_')}` LIKE %s"
            cursor.execute(sql, ('%' + keyword + '%',))

        i = 0
        for row in cursor.fetchall():
            tree.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")


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

    createMainWindow(cursor, TABLE_NAME)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'connection' in locals() or 'connection' in globals():
        connection.close()
