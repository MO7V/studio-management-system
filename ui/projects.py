import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database
from ui.utils import sanitize_row, clear_entries, style_button


def load_projects(project_table):
    projects = database.get_projects()

    for project in projects:
        project_table.insert("", "end", values=sanitize_row(project))


def create_project(project_table):
    title = title_entry.get().strip()
    description = description_entry.get().strip()
    status = status_entry.get().strip()
    customer_id = customer_id_entry.get().strip()

    if not title or not status:
        messagebox.showwarning("Missing information", "Title and status are required.")
        return

    if customer_id and not customer_id.isdigit():
        messagebox.showwarning(
            "Invalid value", "Customer ID must be a number, or left blank."
        )
        return

    try:
        database.add_project(title, description, status, customer_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Invalid customer", f"No customer with ID {customer_id} exists."
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not add project:\n{error}")
        return

    for item in project_table.get_children():
        project_table.delete(item)

    load_projects(project_table)
    clear_entries(title_entry, description_entry, status_entry, customer_id_entry)


def select_project(project_table):
    selected = project_table.selection()

    if not selected:
        return

    project = project_table.item(selected[0])["values"]

    title_entry.delete(0, tk.END)
    title_entry.insert(0, project[1])

    description_entry.delete(0, tk.END)
    description_entry.insert(0, project[2])

    status_entry.delete(0, tk.END)
    status_entry.insert(0, project[3])

    customer_id_entry.delete(0, tk.END)
    customer_id_entry.insert(0, project[4])


def edit_project(project_table):
    selected = project_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a project from the list first.")
        return

    project = project_table.item(selected[0])["values"]
    project_id = project[0]

    title = title_entry.get().strip()
    description = description_entry.get().strip()
    status = status_entry.get().strip()
    customer_id = customer_id_entry.get().strip()

    if not title or not status:
        messagebox.showwarning("Missing information", "Title and status are required.")
        return

    if customer_id and not customer_id.isdigit():
        messagebox.showwarning(
            "Invalid value", "Customer ID must be a number, or left blank."
        )
        return

    try:
        database.update_project(title, description, status, customer_id, project_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Invalid customer", f"No customer with ID {customer_id} exists."
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not update project:\n{error}")
        return

    for item in project_table.get_children():
        project_table.delete(item)

    load_projects(project_table)
    clear_entries(title_entry, description_entry, status_entry, customer_id_entry)


def delete_project_gui(project_table):
    selected = project_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a project from the list first.")
        return

    project = project_table.item(selected[0])["values"]
    project_id = project[0]

    if not messagebox.askyesno(
        "Delete project", f"Delete project '{project[1]}'? This cannot be undone."
    ):
        return

    try:
        database.delete_project(project_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Cannot delete",
            "This project still has tasks linked to it.\n"
            "Remove or reassign those tasks first.",
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not delete project:\n{error}")
        return

    for item in project_table.get_children():
        project_table.delete(item)

    load_projects(project_table)
    clear_entries(title_entry, description_entry, status_entry, customer_id_entry)


def show_project(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR):

    global title_entry
    global description_entry
    global status_entry
    global customer_id_entry

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

    project_table = ttk.Treeview(
        table_frame,
        columns=("id", "title", "description", "status", "customer_id"),
        show="headings",
    )

    project_table.heading("id", text="ID")
    project_table.heading("title", text="Title")
    project_table.heading("description", text="Description")
    project_table.heading("status", text="Status")
    project_table.heading("customer_id", text="Customer ID")

    project_table.column("id", width=50, stretch=False)

    project_table.column("title", width=150)

    project_table.column("description", width=220)

    project_table.column("status", width=120)

    project_table.column("customer_id", width=100)

    project_table.bind("<ButtonRelease-1>", lambda event: select_project(project_table))

    scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=project_table.yview
    )
    project_table.configure(yscrollcommand=scrollbar.set)

    project_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    load_projects(project_table)

    project_title = tk.Label(
        form_frame,
        text="Projects",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
    )

    project_title.pack(anchor="w", padx=15, pady=15)

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

    customer_id_label = tk.Label(
        form_frame,
        text="Customer ID",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 16, "bold"),
    )

    customer_id_label.pack(anchor="w", padx=5)

    customer_id_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    customer_id_entry.pack(padx=20, pady=(15, 5), anchor="w")

    add_project_button = tk.Button(
        form_frame,
        width=25,
        text="Add Project",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: create_project(project_table),
    )
    style_button(add_project_button, "#2ea043", "#3fb950")

    add_project_button.pack(anchor="w", padx=20, pady=10)

    edit_project_button = tk.Button(
        form_frame,
        width=25,
        text="Edit Project",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: edit_project(project_table),
    )
    style_button(edit_project_button, "#0e639c", "#1177bb")

    edit_project_button.pack(anchor="w", padx=20, pady=10)

    delete_project_button = tk.Button(
        form_frame,
        width=25,
        text="Delete Project",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: delete_project_gui(project_table),
    )
    style_button(delete_project_button, "#c0392b", "#e74c3c")

    delete_project_button.pack(anchor="w", padx=20, pady=10)
