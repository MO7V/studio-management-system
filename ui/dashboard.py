import tkinter as tk
import database


def show_dashboard(content, BG_COLOR, TEXT_COLOR, BUTTON_COLOR):

    title = tk.Label(
        content,
        text="Dashboard",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold"),
    )
    title.pack(anchor="w", padx=20, pady=20)

    customers = database.Connection.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    employees = database.Connection.execute(
        "SELECT COUNT(*) FROM employees"
    ).fetchone()[0]

    projects = database.Connection.execute("SELECT COUNT(*) FROM projects").fetchone()[
        0
    ]

    active_projects = database.Connection.execute(
        "SELECT COUNT(*) FROM projects WHERE status = 'Active'"
    ).fetchone()[0]

    tasks = database.Connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]

    completed_tasks = database.Connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Completed'"
    ).fetchone()[0]

    cards_frame = tk.Frame(content, bg=BG_COLOR)
    cards_frame.pack(fill="x", padx=20, pady=20)

    create_card(
        cards_frame, "Customers", customers, BG_COLOR, TEXT_COLOR, BUTTON_COLOR, 0
    )

    create_card(
        cards_frame, "Employees", employees, BG_COLOR, TEXT_COLOR, BUTTON_COLOR, 1
    )

    create_card(
        cards_frame, "Projects", projects, BG_COLOR, TEXT_COLOR, BUTTON_COLOR, 2
    )

    create_card(
        cards_frame,
        "Active Projects",
        active_projects,
        BG_COLOR,
        TEXT_COLOR,
        BUTTON_COLOR,
        3,
    )

    create_card(cards_frame, "Tasks", tasks, BG_COLOR, TEXT_COLOR, BUTTON_COLOR, 4)

    create_card(
        cards_frame,
        "Completed Tasks",
        completed_tasks,
        BG_COLOR,
        TEXT_COLOR,
        BUTTON_COLOR,
        5,
    )


def create_card(parent, title, value, BG_COLOR, TEXT_COLOR, BUTTON_COLOR, column):

    card = tk.Frame(
        parent,
        bg=BUTTON_COLOR,
        width=170,
        height=120,
        border=1,
    )

    card.grid(row=0, column=column, padx=8, pady=8)

    card.pack_propagate(False)

    title_label = tk.Label(
        card, text=title, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 11, "bold")
    )

    title_label.pack(pady=(20, 5))

    value_label = tk.Label(
        card,
        text=str(value),
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 24, "bold"),
    )

    value_label.pack()
