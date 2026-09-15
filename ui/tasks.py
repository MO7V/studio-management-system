import tkinter as tk


def show_task(content, BG_COLOR, TEXT_COLOR):
    task_title = tk.Label(
        content,
        text="Tasks",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold")
    )

    task_title.pack(
        anchor="w",
        padx=20,
        pady=20
    )