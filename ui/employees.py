import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database
from ui.utils import sanitize_row, clear_entries, style_button


def load_employees(employee_table):
    employees = database.get_employee()

    for employee in employees:
        employee_table.insert("", "end", values=sanitize_row(employee))


def create_employee(employee_table):
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    role = role_entry.get().strip()

    if not name or not phone or not role:
        messagebox.showwarning(
            "Missing information", "Name, phone and role are required."
        )
        return

    try:
        database.add_employee(name, phone, email, role)
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not add employee:\n{error}")
        return

    for item in employee_table.get_children():
        employee_table.delete(item)

    load_employees(employee_table)
    clear_entries(name_entry, phone_entry, email_entry, role_entry)


def select_employee(employee_table):
    selected = employee_table.selection()

    if not selected:
        return

    employee = employee_table.item(selected[0])["values"]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, employee[1])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, employee[2])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, employee[3])

    role_entry.delete(0, tk.END)
    role_entry.insert(0, employee[4])


def edit_employee(employee_table):
    selected = employee_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select an employee from the list first.")
        return

    employee = employee_table.item(selected[0])["values"]
    employee_id = employee[0]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    role = role_entry.get().strip()

    if not name or not phone or not role:
        messagebox.showwarning(
            "Missing information", "Name, phone and role are required."
        )
        return

    try:
        database.update_employee(name, phone, email, role, employee_id)
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not update employee:\n{error}")
        return

    for item in employee_table.get_children():
        employee_table.delete(item)

    load_employees(employee_table)
    clear_entries(name_entry, phone_entry, email_entry, role_entry)


def delete_employee_gui(employee_table):
    selected = employee_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select an employee from the list first.")
        return

    employee = employee_table.item(selected[0])["values"]
    employee_id = employee[0]

    if not messagebox.askyesno(
        "Delete employee", f"Delete employee '{employee[1]}'? This cannot be undone."
    ):
        return

    try:
        database.delete_employee(employee_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Cannot delete",
            "This employee still has tasks assigned to them.\n"
            "Remove or reassign those tasks first.",
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not delete employee:\n{error}")
        return

    for item in employee_table.get_children():
        employee_table.delete(item)

    load_employees(employee_table)
    clear_entries(name_entry, phone_entry, email_entry, role_entry)


def show_employee(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR):

    global name_entry
    global phone_entry
    global email_entry
    global role_entry

    form_frame = tk.Frame(content, bg=BG_COLOR)

    form_frame.pack(side="left", fill="y", padx=20, pady=20)

    list_frame = tk.Frame(content, bg=BG_COLOR)

    list_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        background="#252526",
        foreground="#ffffff",
        fieldbackground="#252526",
        rowheight=32,
    )

    style.configure("Treeview.Heading", background="#2d2d30", foreground="#ffffff")

    style.map(
        "Treeview",
        background=[("selected", "#767E8F")],
        foreground=[("selected", "#ffffff")],
    )

    table_frame = tk.Frame(list_frame, bg=BG_COLOR)
    table_frame.pack(fill="both", expand=True)

    employee_table = ttk.Treeview(
        table_frame, columns=("id", "name", "phone", "email", "role"), show="headings"
    )

    employee_table.heading("id", text="ID")

    employee_table.heading("name", text="Name")

    employee_table.heading("phone", text="Phone")

    employee_table.heading("email", text="Email")

    employee_table.heading("role", text="Role")

    employee_table.column("id", width=50, stretch=False)

    employee_table.column("name", width=120)

    employee_table.column("phone", width=120)

    employee_table.column("email", width=180)

    employee_table.column("role", width=120)

    employee_table.bind(
        "<ButtonRelease-1>", lambda event: select_employee(employee_table)
    )

    scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=employee_table.yview
    )
    employee_table.configure(yscrollcommand=scrollbar.set)

    employee_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    load_employees(employee_table)

    employee_title = tk.Label(
        form_frame,
        text="Employees",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
    )

    employee_title.pack(anchor="w", padx=15, pady=15)

    name_label = tk.Label(
        form_frame,
        text="Name",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    name_label.pack(anchor="w", padx=5)

    name_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    name_entry.pack(padx=20, pady=(15, 5), anchor="w")

    phone_label = tk.Label(
        form_frame,
        text="Phone Number",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    phone_label.pack(anchor="w", padx=5)

    phone_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    phone_entry.pack(padx=20, pady=(15, 5), anchor="w")

    email_label = tk.Label(
        form_frame,
        text="Email",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    email_label.pack(anchor="w", padx=5)

    email_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    email_entry.pack(padx=20, pady=(15, 5), anchor="w")

    role_label = tk.Label(
        form_frame,
        text="Role",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    role_label.pack(anchor="w", padx=5)

    role_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    role_entry.pack(padx=20, pady=(15, 5), anchor="w")

    add_employee_button = tk.Button(
        form_frame,
        width=25,
        text="Add Employee",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: create_employee(employee_table),
    )
    style_button(add_employee_button, "#2ea043", "#3fb950")

    add_employee_button.pack(anchor="w", padx=20, pady=10)

    edit_employee_button = tk.Button(
        form_frame,
        width=25,
        text="Edit Employee",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: edit_employee(employee_table),
    )
    style_button(edit_employee_button, "#0e639c", "#1177bb")

    edit_employee_button.pack(anchor="w", padx=20, pady=10)

    delete_employee_button = tk.Button(
        form_frame,
        width=25,
        text="Delete Employee",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: delete_employee_gui(employee_table),
    )
    style_button(delete_employee_button, "#c0392b", "#e74c3c")

    delete_employee_button.pack(anchor="w", padx=20, pady=10)
