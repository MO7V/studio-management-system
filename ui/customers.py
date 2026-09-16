import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database
from ui.utils import sanitize_row, clear_entries, style_button


def create_customer(customer_table):
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    company = company_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Missing information", "Name and phone are required.")
        return

    try:
        database.add_customer(name, phone, email, company)
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not add customer:\n{error}")
        return

    for item in customer_table.get_children():
        customer_table.delete(item)

    load_customers(customer_table)
    clear_entries(name_entry, phone_entry, email_entry, company_entry)


def load_customers(customer_table):
    customers = database.get_customers()

    for customer in customers:
        customer_table.insert("", "end", values=sanitize_row(customer))


def select_customer(customer_table):
    selected = customer_table.selection()

    if not selected:
        return

    customer = customer_table.item(selected[0])["values"]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, customer[1])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, customer[2])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, customer[3])

    company_entry.delete(0, tk.END)
    company_entry.insert(0, customer[4])


def edit_customer(customer_table):
    selected = customer_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a customer from the list first.")
        return

    customer = customer_table.item(selected[0])["values"]
    customer_id = customer[0]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    company = company_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Missing information", "Name and phone are required.")
        return

    try:
        database.update_customers(name, phone, email, company, customer_id)
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not update customer:\n{error}")
        return

    for item in customer_table.get_children():
        customer_table.delete(item)

    load_customers(customer_table)
    clear_entries(name_entry, phone_entry, email_entry, company_entry)


def delete_customer_gui(customer_table):
    selected = customer_table.selection()

    if not selected:
        messagebox.showinfo("No selection", "Select a customer from the list first.")
        return

    customer = customer_table.item(selected[0])["values"]
    customer_id = customer[0]

    if not messagebox.askyesno(
        "Delete customer", f"Delete customer '{customer[1]}'? This cannot be undone."
    ):
        return

    try:
        database.delete_customer(customer_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Cannot delete",
            "This customer still has projects linked to them.\n"
            "Remove or reassign those projects first.",
        )
        return
    except sqlite3.Error as error:
        messagebox.showerror("Database error", f"Could not delete customer:\n{error}")
        return

    for item in customer_table.get_children():
        customer_table.delete(item)

    load_customers(customer_table)
    clear_entries(name_entry, phone_entry, email_entry, company_entry)


def create_customer_form(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR):

    global name_entry
    global phone_entry
    global email_entry
    global company_entry

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

    customer_table = ttk.Treeview(
        table_frame,
        columns=("id", "name", "phone", "email", "company"),
        show="headings",
    )

    customer_table.heading("id", text="ID")

    customer_table.heading("name", text="Name")

    customer_table.heading("phone", text="Phone")

    customer_table.heading("email", text="Email")

    customer_table.heading("company", text="Company")

    customer_table.column("id", width=50, stretch=False)

    customer_table.column("name", width=120)

    customer_table.column("phone", width=120)

    customer_table.column("email", width=180)

    customer_table.column("company", width=120)

    customer_table.bind(
        "<ButtonRelease-1>", lambda event: select_customer(customer_table)
    )

    scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=customer_table.yview
    )
    customer_table.configure(yscrollcommand=scrollbar.set)

    customer_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    load_customers(customer_table)

    customers_title = tk.Label(
        form_frame,
        text="Customers",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
        padx=15,
        pady=15,
    )

    customers_title.pack(anchor="w")

    name_label = tk.Label(
        form_frame,
        text="Name",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR,
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
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR,
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
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR,
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

    company_label = tk.Label(
        form_frame,
        text="Company",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR,
    )

    company_label.pack(anchor="w", padx=5)

    company_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23,
    )

    company_entry.pack(padx=20, pady=(15, 5), anchor="w")

    add_customer_button = tk.Button(
        form_frame,
        width=25,
        text="Add Customer",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: create_customer(customer_table),
    )
    style_button(add_customer_button, "#2ea043", "#3fb950")

    add_customer_button.pack(anchor="w", padx=20, pady=10)

    edit_customer_button = tk.Button(
        form_frame,
        width=25,
        text="Edit Customer",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: edit_customer(customer_table),
    )
    style_button(edit_customer_button, "#0e639c", "#1177bb")

    edit_customer_button.pack(anchor="w", padx=20, pady=10)

    delete_customer_button = tk.Button(
        form_frame,
        width=25,
        text="Delete Customer",
        fg=TEXT_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: delete_customer_gui(customer_table),
    )
    style_button(delete_customer_button, "#c0392b", "#e74c3c")

    delete_customer_button.pack(anchor="w", padx=20, pady=10)
