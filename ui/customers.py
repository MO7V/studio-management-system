import tkinter as tk
import database


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

    customers_title = tk.Label(
        content,
        text="Customers",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
        padx=20,
        pady=20
    )

    customers_title.pack(anchor="w")


    name_label = tk.Label(
        content,
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
        content,
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
        content,
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
        content,
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
        content,
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
        content,
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
        content,
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
        content,
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
        content,
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