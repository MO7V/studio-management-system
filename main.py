import database
import tkinter as tk 



# database.add_customer("mmd","0910","ggg@gmile","azar")
def create_customer():
    

    name = name_entry.get()
    phone = phone_entry.get()
    if not name or not phone:
        print("name and phone are required.")
        return
    email = email_entry.get()
    company = company_entry.get()

    database.add_customer(name, phone, email, company)


def show_customers():

    customers = database.get_customers()

    for customer in customers:
        print(customer)


def edit_customer():

    id_c = input("customer id: ")

    if not id_c.isdigit():
        print("id must be a number.")
        return

    name = input("your name: ")
    phone = input("your number: ")

    if not name or not phone:
        print("name and phone are required.")
        return

    email = input("your email: ")
    company = input("your company: ")

    database.update_customers(name, phone, email, company, id_c)


def remove_customer():

    id_c = input("id for delete: ")

    if not id_c.isdigit():
        print("id must be a number.")
        return

    database.delete_customer(id_c)


def create_employee():

    name = input("your name: ")
    phone = input("your number: ")
    role = input("your role: ")

    if not name or not phone or not role:
        print("name, phone and role are required.")
        return

    email = input("your email: ")

    database.add_employee(name, phone, email, role)


def show_employees():

    employees = database.get_employee()

    for employee in employees:
        print(employee)


def edit_employee():

    id_e = input("employee id: ")

    if not id_e.isdigit():
        print("id must be a number.")
        return

    name = input("your name: ")
    phone = input("your number: ")
    role = input("your role: ")

    if not name or not phone or not role:
        print("name, phone and role are required.")
        return

    email = input("your email: ")

    database.update_employee(name, phone, email, role, id_e)


def remove_employee():

    id_e = input("id for delete employee: ")

    if not id_e.isdigit():
        print("id must be a number.")
        return

    database.delete_employee(id_e)


def create_project():

    title = input("title: ")
    description = input("description: ")
    status = input("status: ")
    customer_id = input("customer_id: ")

    if not title or not status:
        print("title and status are required.")
        return

    if not customer_id.isdigit():
        print("customer_id must be a number.")
        return

    database.add_project(title, description, status, customer_id)


def show_projects():

    projects = database.get_projects()

    for project in projects:
        print(project)


def edit_project():

    id_p = input("id: ")

    if not id_p.isdigit():
        print("id must be a number.")
        return

    title = input("title: ")
    description = input("description: ")
    status = input("status: ")
    customer_id = input("customer_id: ")

    if not title or not status:
        print("title and status are required.")
        return

    if not customer_id.isdigit():
        print("customer_id must be a number.")
        return

    database.update_project(title, description, status, customer_id, id_p)


def remove_project():

    id_p = input("id for delete project: ")

    if not id_p.isdigit():
        print("id must be a number.")
        return

    database.delete_project(id_p)


def create_task():

    title = input("title: ")
    description = input("description: ")
    status = input("status: ")
    project_id = input("project_id: ")
    employee_id = input("employee_id: ")

    if not title or not status:
        print("title and status are required.")
        return

    if not project_id.isdigit() or not employee_id.isdigit():
        print("project_id and employee_id must be numbers.")
        return

    database.add_task(title, description, status, project_id, employee_id)


def show_tasks():

    tasks = database.get_tasks()

    for task in tasks:
        print(task)


def edit_task():

    id_t = input("id: ")

    if not id_t.isdigit():
        print("id must be a number.")
        return

    title = input("title: ")
    description = input("description: ")
    status = input("status: ")
    project_id = input("project_id: ")
    employee_id = input("employee_id: ")

    if not title or not status:
        print("title and status are required.")
        return

    if not project_id.isdigit() or not employee_id.isdigit():
        print("project_id and employee_id must be numbers.")
        return

    database.update_task(title, description, status, project_id, employee_id, id_t)


def remove_task():

    id_t = input("id for delete task: ")

    if not id_t.isdigit():
        print("id must be a number.")
        return

    database.delete_task(id_t)




# 000000000000000000000000000000000
import tkinter as tk

from ui.customers import create_customer_form
from ui.dashboard import show_dashboard
from ui.employees import show_employee
from ui.projects import show_project
from ui.tasks import show_task
def clear_content():
    for widgat in content.winfo_children():
        widgat.destroy()
root = tk.Tk()

BG_COLOR = "#1e1e1e"
SIDEBAR_COLOR = "#252526"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#2d2d30"

root.title("Studio Management System")
root.geometry("1400x800")
root.configure(bg=BG_COLOR)


# Sidebar
sidebar = tk.Frame(
    root,
    bg=SIDEBAR_COLOR,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


title = tk.Label(
    sidebar,
    text="Studio Management",
    bg=SIDEBAR_COLOR,
    fg=TEXT_COLOR,
    font=("Segoe UI", 16, "bold")
)

title.pack(pady=30)


# Sidebar Buttons

dashboard_button = tk.Button(
    sidebar,
    text="Dashboard",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#3a3a3d",
    activeforeground=TEXT_COLOR,
    borderwidth=1,
    relief="solid",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2",
    command=lambda: (
    clear_content(),
    show_dashboard(content, BG_COLOR, TEXT_COLOR)
)
)

dashboard_button.pack(
    fill="x",
    padx=15,
    pady=5
)


customers_button = tk.Button(
    sidebar,
    text="Customers",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#3a3a3d",
    activeforeground=TEXT_COLOR,
    borderwidth=1,
    relief="solid",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2",
    command=lambda: (
    clear_content(),
    create_customer_form(
        content,
        BG_COLOR,
        TEXT_COLOR,
        BUTTON_COLOR
    )
)

)

customers_button.pack(
    fill="x",
    padx=15,
    pady=5
)


projects_button = tk.Button(
    sidebar,
    text="Projects",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#3a3a3d",
    activeforeground=TEXT_COLOR,
    borderwidth=1,
    relief="solid",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2",
    command=lambda: (
    clear_content(),
    show_project(content, BG_COLOR, TEXT_COLOR)
)
)


projects_button.pack(
    fill="x",
    padx=15,
    pady=5
)


employees_button = tk.Button(
    sidebar,
    text="Employees",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#3a3a3d",
    activeforeground=TEXT_COLOR,
    borderwidth=1,
    relief="solid",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2",
    command=lambda: (
    clear_content(),
    show_employee(content, BG_COLOR, TEXT_COLOR)
)
)

employees_button.pack(
    fill="x",
    padx=15,
    pady=5
)


tasks_button = tk.Button(
    sidebar,
    text="Tasks",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#3a3a3d",
    activeforeground=TEXT_COLOR,
    borderwidth=1,
    relief="solid",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2",
    command=lambda: (
    clear_content(),
    show_task(content, BG_COLOR, TEXT_COLOR)
)
)


tasks_button.pack(
    fill="x",
    padx=15,
    pady=5
)


# Main Content

content = tk.Frame(
    root,
    bg=BG_COLOR
)

content.pack(
    side="left",
    fill="both",
    expand=True
)


# Customers page
create_customer_form(
    content,
    BG_COLOR,
    TEXT_COLOR,
    BUTTON_COLOR
)


root.mainloop()

# ____________TESTS_____________

# print("=== CUSTOMER TEST ===")

# create_customer()
# show_customers()


# print("\n=== EMPLOYEE TEST ===")

# create_employee()
# show_employees()


# print("\n=== PROJECT TEST ===")

# create_project()
# show_projects()


# print("\n=== TASK TEST ===")

# create_task()
# show_tasks()
