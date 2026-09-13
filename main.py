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


for customer in get_customers():
    print(customer)


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


Connection.close()
