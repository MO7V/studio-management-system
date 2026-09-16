import tkinter as tk


def sanitize_row(row):
    return tuple("" if value is None else value for value in row)


def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)


def style_button(button, base_color, hover_color):
    button.configure(bg=base_color, activebackground=hover_color)
    button.bind("<Enter>", lambda e: button.configure(bg=hover_color))
    button.bind("<Leave>", lambda e: button.configure(bg=base_color))
