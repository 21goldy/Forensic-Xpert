import os
import psutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from StaticGUIConfigs import *

def run_pslist_tool(parent_window):
    root = tk.Toplevel(parent_window)
    root.title("Process List View")
    root.resizable(False, False) # Disallow resizing of the mainWindow
    root['background']=bgColor # Set backgound color 
    
    # Output window
    process_list_text = tk.Text(
        root,
        height=20,
        width=50,
        wrap=tk.WORD,
        background="lightblue")
    process_list_text.pack()

    display_process_list(process_list_text) # Display process list function

    # Button to export to a file
    export_button = tk.Button(
        root,
        text="Export to File",
        command=lambda: export_to_file(process_list_text.get("1.0", tk.END)),
        background="darkgray",
        padx=10,
        pady=5)
    export_button.pack(pady=10)

    root.mainloop()

def display_process_list(text_widget):
    processes = get_process_list()
    text_widget.delete(1.0, tk.END)  # Clear previous content
    for process in processes:
        text_widget.insert(tk.END, f"PID: {process['pid']}, Name: {process['name']}\n")

def get_process_list():
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        processes.append({'pid': process.info['pid'], 'name': process.info['name']})
    return processes

def export_to_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Export Successful", "Export to file was successful!")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting to file: {e}")

# if __name__ == "__main__":
#     run_pslist_tool()
