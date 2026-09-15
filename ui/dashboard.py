import tkinter as tk


def show_dashboard(content, BG_COLOR, TEXT_COLOR):
    dashboard_title = tk.Label(
        content,
        text="Dashboard",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 26, "bold")
    )

    dashboard_title.pack(
        anchor="w",
        padx=20,
        pady=20
    )