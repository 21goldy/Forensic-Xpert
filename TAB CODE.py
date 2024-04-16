import tkinter as tk
from tkinter import ttk

def create_tab(tab_name):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)
    label = ttk.Label(tab, text=f"Content for {tab_name}")
    label.pack(padx=10, pady=10)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

root = tk.Tk()
root.title("Tab Example")

notebook = ttk.Notebook(root)

# Create tabs
create_tab("Web Browser Forensics")
create_tab("Image Forensics")
create_tab("Tab 3")

notebook.pack(expand=True, fill="both")

# Center the window on the screen
width = 600  # specify the width of your window
height = 400  # specify the height of your window
center_window(root, width, height)

root.mainloop()
