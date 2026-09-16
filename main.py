import tkinter as tk

from ui.customers import create_customer_form
from ui.dashboard import show_dashboard
from ui.employees import show_employee
from ui.projects import show_project
from ui.tasks import show_task

BG_COLOR = "#1e1e1e"
SIDEBAR_COLOR = "#252526"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#2d2d30"
ACTIVE_COLOR = "#0e639c"
HOVER_COLOR = "#3a3a3d"


def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def set_active(button):
    for b in sidebar_buttons:
        b.configure(bg=ACTIVE_COLOR if b is button else BUTTON_COLOR)


def make_nav_button(text, page_loader):
    button = tk.Button(
        sidebar,
        text=text,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=HOVER_COLOR,
        activeforeground=TEXT_COLOR,
        borderwidth=1,
        relief="solid",
        font=("Segoe UI", 11, "bold"),
        cursor="hand2",
    )

    def on_click():
        clear_content()
        page_loader(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR)
        set_active(button)

    button.configure(command=on_click)

    button.bind(
        "<Enter>",
        lambda e: (
            button.configure(bg=HOVER_COLOR) if button["bg"] != ACTIVE_COLOR else None
        ),
    )
    button.bind(
        "<Leave>",
        lambda e: (
            button.configure(bg=BUTTON_COLOR) if button["bg"] != ACTIVE_COLOR else None
        ),
    )

    button.pack(fill="x", padx=15, pady=5)

    return button


root = tk.Tk()
root.title("Studio Management System")
root.geometry("1400x800")
root.minsize(1100, 650)
root.configure(bg=BG_COLOR)


# Sidebar
sidebar = tk.Frame(root, bg=SIDEBAR_COLOR, width=220)

sidebar.pack(side="left", fill="y")

sidebar.pack_propagate(False)


title = tk.Label(
    sidebar,
    text="Studio Management",
    bg=SIDEBAR_COLOR,
    fg=TEXT_COLOR,
    font=("Segoe UI", 16, "bold"),
)

title.pack(pady=30)
content = tk.Frame(root, bg=BG_COLOR)

content.pack(side="left", fill="both", expand=True)


dashboard_button = make_nav_button("Dashboard", show_dashboard)
customers_button = make_nav_button("Customers", create_customer_form)
projects_button = make_nav_button("Projects", show_project)
employees_button = make_nav_button("Employees", show_employee)
tasks_button = make_nav_button("Tasks", show_task)

sidebar_buttons = [
    dashboard_button,
    customers_button,
    projects_button,
    employees_button,
    tasks_button,
]


create_customer_form(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR)
set_active(customers_button)


root.mainloop()
