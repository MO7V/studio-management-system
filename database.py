import sqlite3

Connection = sqlite3.connect("studio.db")
Connection.execute("PRAGMA foreign_keys = ON")

Connection.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT NOT NULL, 
    email TEXT,
    company TEXT
)
""")
Connection.execute("""
CREATE TABLE IF NOT EXISTS employees  (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT NOT NULL, 
    email TEXT,
    role TEXT
)
""")
Connection.execute("""
CREATE TABLE IF NOT EXISTS projects  (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT, 
    status TEXT,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
""")
Connection.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT, 
    status TEXT,
    project_id INTEGER,
    employee_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
)
""")

def add_task(title, description, status, project_id, employee_id):
    Connection.execute(
        """
    INSERT INTO tasks (title, description, status, project_id, employee_id)
    VALUES (?, ?, ?, ?, ?)
    """,
        (title, description, status, project_id, employee_id),
    )

    Connection.commit()


def get_tasks():

    result = Connection.execute("SELECT * FROM tasks")

    tasks = result.fetchall()

    return tasks


def update_task(title, description, status, project_id, employee_id, id):
    Connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, status = ?, project_id = ?, employee_id = ?
        WHERE id = ?
        """,
        (title, description, status, project_id, employee_id, id)
    )
    Connection.commit()


def delete_task(id):
    Connection.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (id,)
    )
    Connection.commit()


def add_project(title, description, status, customer_id):
    Connection.execute(
        """
    INSERT INTO projects (title, description, status, customer_id)
    VALUES (?, ?, ?, ?)
    """,
        (title, description, status, customer_id),
    )

    Connection.commit()


def get_projects():
    result = Connection.execute("SELECT * FROM projects")
    project = result.fetchall()
    return project


/
def update_project(title, description, status, customer_id, id):
    Connection.execute(
        """UPDATE projects
    SET title = ?, description = ?, status = ?, customer_id = ?
    WHERE id = ?
    """,
        (title, description, status, customer_id, id),
    )
    Connection.commit()


def delete_project(
    id,
):
    Connection.execute(
        """
    DELETE FROM projects
    WHERE id = ?
    """,
        (id,),
    )
    Connection.commit()


def add_customer(name, phone, email, company):
    Connection.execute(
        """
    INSERT INTO customers (name, phone, email, company)
    VALUES (?, ?, ?, ?)
    """,
        (name, phone, email, company),
    )

    Connection.commit()


def get_customers():
    result = Connection.execute("SELECT * FROM customers")
    customers = result.fetchall()
    return customers





def update_customers(name, phone, email, company, id):
    Connection.execute(
        """UPDATE customers
    SET name = ?,phone = ?,  email = ?,company =?
    WHERE id = ?
    """,
        (name, phone, email, company, id),
    )
    Connection.commit()


def delete_customer(id):
    Connection.execute(
        """
    DELETE FROM customers
    WHERE id = ?
    """,
        (id,),
    )
    Connection.commit()


def add_employee(name, phone, email, role):
    Connection.execute(
        """
    INSERT INTO employees (name, phone, email, role)
    VALUES (?, ?, ?, ?)
    """,
        (name, phone, email, role),
    )

    Connection.commit()


def get_employee():
    result = Connection.execute("SELECT * FROM employees")
    employees = result.fetchall()
    return employees


def update_employee(name, phone, email, role, id):
    Connection.execute(
        """UPDATE employees
    SET name = ?,phone = ?,  email = ?,role =?
    WHERE id = ?
    """,
        (name, phone, email, role, id),
    )
    Connection.commit()


def delete_employee(id):
    Connection.execute(
        """
    DELETE FROM employees
    WHERE id = ?
    """,
        (id,),
    )
    Connection.commit()
    
