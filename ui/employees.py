import tkinter as tk


def show_employee(content, BG_COLOR, TEXT_COLOR):
    employee_title = tk.Label(
        content,
        text="Employee",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold")
    )

    employee_title.pack(
        anchor="w",
        padx=20,
        pady=20
    )