import database


# database.add_customer("mmd","0910","ggg@gmile","azar")
def create_customer():
    name = input("your name:")
    phone = input("your number:")
    email = input("your email:")
    company = input("your company:")
    database.add_customer(name, phone, email, company)


def show_customers():
    customers = database.get_customers()
    for customer in customers:
        print(customer)


def edit_customer():
    id_c = input("customer id :")
    name = input("your name:")
    phone = input("your number:")
    email = input("your email:")
    company = input("your company:")
    database.update_customers(name, phone, email, company, id_c)


def remove_customer():
    id_c = input("id for dellete:")
    database.delete_customer(id_c)


def create_employee():
    name = input("your name:")
    phone = input("your number:")
    email = input("your email:")
    role = input("your role:")
    database.add_employee(name, phone, email, role)


def show_employees():
    employees = database.get_employee()
    for employee in employees:
        print(employee)


def edit_employee():
    id_e = input("empluyee id :")
    name = input("your name:")
    phone = input("your number:")
    email = input("your email:")
    role = input("your role:")
    database.update_customers(name, phone, email, role, id_e)


def remove_employee():
    id_e = input("id for dellete employee:")
    database.delete_employee(id_e)


def create_project():
    title = input("title:")
    description = input("description:")
    status = input("status:")
    customer_id = input("customer_id:")
    database.add_project(title, description, status, customer_id)


def show_projects():
    projects = database.get_projects()
    for project in projects:
        print(project)


def edit_project():
    id_p = input("id:")
    title = input("title:")
    description = input("description:")
    status = input("status:")
    customer_id = input("customer_id:")
    database.update_project(title, description, status, customer_id, id_p)


def remove_project():
    id_p = input("id for dellete project:")
    database.delete_project(id_p)


def create_task():
    id_t = input("id:")
    title = input("title:")
    description = input("description:")
    status = input("status:")
    project_id = input("project_id")
    employee_id = input("employee_id:")
    database.add_task(title, description, status, project_id, employee_id)


def show_tasks():
    tasks = database.get_tasks()
    for task in tasks:
        print(task)


def edit_task():
    id_t = input("id:")
    title = input("title:")
    description = input("description:")
    status = input("status:")
    project_id = input("project_id")
    employee_id = input("employee_id:")
    database.update_task(title, description, status, project_id, employee_id, id_t)


def remove_task():
    id_p = input("id for dellete tasks:")
    database.delete_task(id_p)
