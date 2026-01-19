import tkinter as tk
from tkinter import messagebox

# Dummy credentials (replace with database check later)
users = {
    "admin": "admin123",
    "teacher": "teach2026",
    "student": "stud2026"
}

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        # Here you can open attendance dashboard window
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# GUI setup
root = tk.Tk()
root.title("Attendance Management System - Login")
root.geometry("350x200")

# Labels and Entries
tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
