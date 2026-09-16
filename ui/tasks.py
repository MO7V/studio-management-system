import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database
from ui.utils import sanitize_row, clear_entries, style_button


def load_tasks(task_table):
    tasks = database.get_tasks()

    for task in tasks:
        task_table.insert("", "end", values=sanitize_row(task))


def _validate_task_form(title, status, project_id, employee_id):
    if not title or not status:
        messagebox.showwarning("Missing information", "Title and status are required.")
        return False

    if project_id and not project_id.isdigit():
        messagebox.showwarning(
            "Invalid value", "Project ID must be a number, or left blank."
        )
        return False

    if employee_id and not employee_id.isdigit():
        messagebox.showwarning(
            "Invalid value", "Employee ID must be a number, or left blank."
        )
        return False

    return True


def create_task(task_table):
    title = title_entry.get().strip()
    description = description_entry.get().strip()
    status = status_entry.get().strip()
    project_id = project_id_entry.get().strip()
    employee_id = employee_id_entry.get().strip()

    if not _validate_task_form(title, status, project_id, employee_id):
        return

    try:
        database.add_task(title, description, status, project_id, employee_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Invalid reference",
            "The Project ID or Employee ID given doesn't match an existing record.",
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not add task:\n{error}")
        return

    for item in task_table.get_children():
        task_table.delete(item)

    load_tasks(task_table)
    clear_entries(
        title_entry,
        description_entry,
        status_entry,
        project_id_entry,
        employee_id_entry,
    )


def select_task(task_table):
    selected = task_table.selection()

    if not selected:
        return

    task = task_table.item(selected[0])["values"]

    title_entry.delete(0, tk.END)
    title_entry.insert(0, task[1])

    description_entry.delete(0, tk.END)
    description_entry.insert(0, task[2])

    status_entry.delete(0, tk.END)
    status_entry.insert(0, task[3])

    project_id_entry.delete(0, tk.END)
    project_id_entry.insert(0, task[4])

    employee_id_entry.delete(0, tk.END)
    employee_id_entry.insert(0, task[5])


def edit_task(task_table):
    selected = task_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a task from the list first.")
        return

    task = task_table.item(selected[0])["values"]
    task_id = task[0]

    title = title_entry.get().strip()
    description = description_entry.get().strip()
    status = status_entry.get().strip()
    project_id = project_id_entry.get().strip()
    employee_id = employee_id_entry.get().strip()

    if not _validate_task_form(title, status, project_id, employee_id):
        return

    try:
        database.update_task(
            title, description, status, project_id, employee_id, task_id
        )
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Invalid reference",
            "The Project ID or Employee ID given doesn't match an existing record.",
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not update task:\n{error}")
        return

    for item in task_table.get_children():
        task_table.delete(item)

    load_tasks(task_table)
    clear_entries(
        title_entry,
        description_entry,
        status_entry,
        project_id_entry,
        employee_id_entry,
    )


def delete_task_ui(task_table):
    selected = task_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a task from the list first.")
        return

    task = task_table.item(selected[0])["values"]
    task_id = task[0]

    if not messagebox.askyesno(
        "Delete task", f"Delete task '{task[1]}'? This cannot be undone."
    ):
        return

    try:
        database.delete_task(task_id)
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not delete task:\n{error}")
        return

    for item in task_table.get_children():
        task_table.delete(item)

    load_tasks(task_table)
    clear_entries(
        title_entry,
        description_entry,
        status_entry,
        project_id_entry,
        employee_id_entry,
    )


def show_task(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR):

    global title_entry
    global description_entry
    global status_entry
    global project_id_entry
    global employee_id_entry

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

    task_table = ttk.Treeview(
        table_frame,
        columns=("id", "title", "description", "status", "project_id", "employee_id"),
        show="headings",
    )

    task_table.heading("id", text="ID")
    task_table.heading("title", text="Title")
    task_table.heading("description", text="Description")
    task_table.heading("status", text="Status")
    task_table.heading("project_id", text="Project ID")
    task_table.heading("employee_id", text="Employee ID")

    task_table.column("id", width=50, stretch=False)

    task_table.column("title", width=140)

    task_table.column("description", width=200)

    task_table.column("status", width=110)

    task_table.column("project_id", width=90)

    task_table.column("employee_id", width=100)

    task_table.bind("<ButtonRelease-1>", lambda event: select_task(task_table))

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=task_table.yview)
    task_table.configure(yscrollcommand=scrollbar.set)

    task_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    load_tasks(task_table)

    tasks_title = tk.Label(
        form_frame,
        text="Tasks",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
    )

    tasks_title.pack(anchor="w", padx=15, pady=15)

    title_label = tk.Label(
        form_frame,
        text="Title",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    title_label.pack(anchor="w", padx=5)

    title_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    title_entry.pack(padx=20, pady=(15, 5), anchor="w")

    description_label = tk.Label(
        form_frame,
        text="Description",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    description_label.pack(anchor="w", padx=5)

    description_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    description_entry.pack(padx=20, pady=(15, 5), anchor="w")

    status_label = tk.Label(
        form_frame,
        text="Status",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    status_label.pack(anchor="w", padx=5)

    status_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    status_entry.pack(padx=20, pady=(15, 5), anchor="w")

    project_id_label = tk.Label(
        form_frame,
        text="Project ID",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    project_id_label.pack(anchor="w", padx=5)

    project_id_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    project_id_entry.pack(padx=20, pady=(15, 5), anchor="w")

    employee_id_label = tk.Label(
        form_frame,
        text="Employee ID",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    employee_id_label.pack(anchor="w", padx=5)

    employee_id_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    employee_id_entry.pack(padx=20, pady=(15, 5), anchor="w")

    add_task_button = tk.Button(
        form_frame,
        width=25,
        text="Add Task",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: create_task(task_table),
    )
    style_button(add_task_button, "#2ea043", "#3fb950")

    add_task_button.pack(anchor="w", padx=20, pady=10)

    edit_task_button = tk.Button(
        form_frame,
        width=25,
        text="Edit Task",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: edit_task(task_table),
    )
    style_button(edit_task_button, "#0e639c", "#1177bb")

    edit_task_button.pack(anchor="w", padx=20, pady=10)

    delete_task_button = tk.Button(
        form_frame,
        width=25,
        text="Delete Task",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: delete_task_ui(task_table),
    )
    style_button(delete_task_button, "#c0392b", "#e74c3c")

    delete_task_button.pack(anchor="w", padx=20, pady=10)
