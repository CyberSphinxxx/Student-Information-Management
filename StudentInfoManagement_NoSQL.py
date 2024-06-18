import tkinter as tk
from tkinter import ttk, messagebox

students_data = []

def displayResults(root):
    def refresh():
        tree.delete(*tree.get_children())
        for i, row in enumerate(students_data):
            tree.insert('', i, text="Student " + str(i + 1), values=row)
        total_students_label.config(text=f"Total Students: {len(students_data)}")

    def search():
        selected_criteria = searchCriteria.get()
        keyword = searchKeyword.get()
        if selected_criteria and keyword:
            tree.delete(*tree.get_children())
            for i, row in enumerate(students_data):
                if keyword.lower() in row[searchCriteria.current()].lower():
                    tree.insert('', i, text="Student " + str(i + 1), values=row)
        else:
            messagebox.showwarning("Warning", "Please select a search criteria and enter a keyword.")

    secondWindow = tk.Toplevel(root)
    secondWindow.title("Admin Panel")

    tk.Label(secondWindow, text="USTP Student Management System", font=("Arial", 24, "bold")).pack(pady=20)

    searchFrame = tk.Frame(secondWindow)
    searchFrame.pack(pady=10, padx=10, fill="x")

    tk.Label(searchFrame, text="Search by:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    searchCriteria = ttk.Combobox(searchFrame, values=("First Name", "Last Name", "Course", "Year Level", "Student ID", "Phone Number"), font=("Arial", 12))
    searchCriteria.grid(row=0, column=1, padx=5)
    searchCriteria.set("First Name")

    tk.Label(searchFrame, text="Keyword:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
    searchKeyword = tk.Entry(searchFrame, font=("Arial", 12))
    searchKeyword.grid(row=0, column=3, padx=5)

    tk.Button(searchFrame, text="Search", font=("Arial", 12), command=search).grid(row=0, column=4, padx=5)
    tk.Button(searchFrame, text="Refresh", font=("Arial", 12), command=refresh).grid(row=0, column=5, padx=5)

    tree = ttk.Treeview(secondWindow, columns=("one", "two", "three", "four", "five", "six"))
    tree.heading("one", text="First Name")
    tree.heading("two", text="Last Name")
    tree.heading("three", text="Course")
    tree.heading("four", text="Year Level")
    tree.heading("five", text="Student ID")
    tree.heading("six", text="Phone Number")

    for i, row in enumerate(students_data):
        tree.insert('', i, text="Student " + str(i + 1), values=row)

    total_students_label = tk.Label(secondWindow, text=f"Total Students: {len(students_data)}", font=("Arial", 12))
    total_students_label.pack(pady=10)

    tree.pack(expand=True, fill="both")
    tk.Button(secondWindow, text="Back", font=("Arial", 12), command=secondWindow.destroy).pack(pady=20)

def createMainWindow():
    def takeNameInput(*entries):
        data = [entry.get() for entry in entries]
        if all(data):
            students_data.append(tuple(data))
            for entry in entries:
                entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Data Saved Successfully.")
        else:
            messagebox.showwarning("Warning", "Please fill all the necessary information to proceed.")

    root = tk.Tk()
    root.title("Student Information System")

    tk.Label(root, text="USTP Student Information System", font=("Arial", 24, "bold"), fg="#06a099").grid(row=0, columnspan=2, pady=30)

    labels = ["First Name:", "Last Name:", "Course:", "Year Level:", "Student ID:", "Phone Number:"]
    entries = []
    for idx, label_text in enumerate(labels):
        tk.Label(root, text=label_text, font=("Arial", 12)).grid(row=idx + 1, column=0, padx=10, pady=10, sticky="w")
        entry = tk.Entry(root, font=("Arial", 12))
        entry.grid(row=idx + 1, column=1, padx=10, pady=10, sticky="ew")
        entries.append(entry)

    tk.Button(root, text="Save Information", font=("Arial", 12), command=lambda: takeNameInput(*entries)).grid(row=len(labels) + 1, columnspan=2, pady=30)
    tk.Button(root, text="Admin Panel", font=("Arial", 12), command=lambda: loginWindow(root)).grid(row=len(labels) + 2, columnspan=2, pady=10)

    for i in range(len(labels) + 3):
        root.grid_rowconfigure(i, weight=1)
    for i in range(2):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

def loginWindow(root):
    loginWindow = tk.Toplevel(root)
    loginWindow.title("Admin Login")

    tk.Label(loginWindow, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    usernameEntry = tk.Entry(loginWindow, font=("Arial", 12))
    usernameEntry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(loginWindow, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
    passwordEntry = tk.Entry(loginWindow, show="*", font=("Arial", 12))
    passwordEntry.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(loginWindow, text="Login", font=("Arial", 12), command=lambda: authenticate(usernameEntry.get(), passwordEntry.get(), loginWindow, root)).grid(row=2, columnspan=2, pady=5)

def authenticate(username, password, loginWindow, root):
    if username == "admin" and password == "admin":
        loginWindow.destroy()
        displayResults(root)
    else:
        messagebox.showerror("Error!", "Invalid username or password")

createMainWindow()
