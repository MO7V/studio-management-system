import tkinter as tk


def show_project(content, BG_COLOR, TEXT_COLOR):
    project_title = tk.Label(
        content,
        text="Projects",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold")
    )

    project_title.pack(
        anchor="w",
        padx=20,
        pady=20
    )