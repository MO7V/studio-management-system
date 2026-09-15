import tkinter as tk
import database
from tkinter import ttk

def create_customer():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    company = company_entry.get()

    database.add_customer(
        name,
        phone,
        email,
        company
    )
def load_customers(customer_table):
    customers = database.get_customers()

    for customer in customers:
        customer_table.insert(
            "",
            "end",
            values=customer
        )


def create_customer_form(
    content,
    BG_COLOR,
    TEXT_COLOR,
    BUTTON_COLOR
):

    global name_entry
    global phone_entry
    global email_entry
    global company_entry



    form_frame = tk.Frame(
        content,
        bg=BG_COLOR
    )
    form_frame.pack(
        side="left",
        fill="y",
        padx=20,
        pady=20
    )

    list_frame = tk.Frame(
        content,
        bg=BG_COLOR
    )
    list_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        background="#252526",
        foreground="#ffffff",
        fieldbackground="#252526",
        rowheight=32
        
    )

    style.configure(
        "Treeview.Heading",
        background="#2d2d30",
        foreground="#ffffff"
    )

    style.map(
        "Treeview",
        background=[("selected", "#767E8F")],
        foreground=[("selected", "#ffffff")]
    )
            
    customer_table = ttk.Treeview(
        list_frame,
        columns=("id", "name", "phone", "email", "company"),
        show="headings"
    )
    customer_table.heading("id", text="ID")
    customer_table.heading("name", text="Name")
    customer_table.heading("phone", text="Phone")
    customer_table.heading("email", text="Email")
    customer_table.heading("company", text="Company")

    customer_table.pack(
        fill="both",
        expand=True
    )
    load_customers(customer_table)

    customers_title = tk.Label(
        form_frame,
        text="Customers",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
        padx=15,
        pady=15
    )

    customers_title.pack(
        anchor="w"
    )

    name_label = tk.Label(
        form_frame,
        text="Name",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR
    )

    name_label.pack(
        anchor="w",
        padx=5
    )

    name_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23
    )

    name_entry.pack(
        padx=20,
        pady=(15, 5),
        anchor="w"
    )

    phone_label = tk.Label(
        form_frame,
        text="Phone Number",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR
    )

    phone_label.pack(
        anchor="w",
        padx=5
    )

    phone_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23
    )

    phone_entry.pack(
        padx=20,
        pady=(15, 5),
        anchor="w"
    )



    email_label = tk.Label(
        form_frame,
        text="Email",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR
    )

    email_label.pack(
        anchor="w",
        padx=5
    )

    email_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23
    )

    email_entry.pack(
        padx=20,
        pady=(15, 5),
        anchor="w"
    )



    company_label = tk.Label(
        form_frame,
        text="Company",
        bg=BG_COLOR,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT_COLOR
    )

    company_label.pack(
        anchor="w",
        padx=5
    )

    company_entry = tk.Entry(
        form_frame,
        bg="#626262",
        fg="#ffffff",
        insertbackground="#ffffff",
        borderwidth=1,
        relief="solid",
        width=23
    )

    company_entry.pack(
        padx=20,
        pady=(15, 5),
        anchor="w"
    )



    add_customer_button = tk.Button(
        form_frame,
        width=25,
        text="Add Customer",
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground="#3a3a3d",
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=create_customer
    )

    add_customer_button.pack(
        anchor="w",
        padx=20,
        pady=10
    )