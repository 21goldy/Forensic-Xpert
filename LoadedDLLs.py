import os
import psutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from StaticGUIConfigs import *

def run_list_loaded_dlls_tool(parent_window):
    root = tk.Toplevel(parent_window)
    root.title("List Loaded DLLs")
    root.resizable(False, False) # Disallow resizing of the mainWindow
    root['background']=bgColor # Set backgound color 

    # Create a style to customize the Treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background=bgColor)
    style.configure("Treeview", font=('Helvetica', 11), background="lightblue")

    # Treeview to display loaded DLLs
    loaded_dlls_tree = ttk.Treeview(
        root,
        columns=("Process ID", "Loaded DLLs"),
        show="headings",
        height=20,
        style="Treeview")
    loaded_dlls_tree.heading("Process ID", text="Process ID")
    loaded_dlls_tree.heading("Loaded DLLs", text="Loaded DLLs")
    loaded_dlls_tree.column("Loaded DLLs", width=500, anchor="w")  # Adjust width as needed
    loaded_dlls_tree.pack()

    # Display loaded DLLs immediately
    display_loaded_dlls(loaded_dlls_tree)

    # Button to export to a file
    export_button = tk.Button(
        root,
        text="Export to File",
        command=lambda: export_to_file(loaded_dlls_tree, "Loaded_DLLs"),
        background="darkgray",
        padx=10,
        pady=5)
    export_button.pack(pady=10)

    root.mainloop()

def display_loaded_dlls(tree):
    loaded_dlls = get_loaded_dlls()
    for process, dlls in loaded_dlls.items():
        dll_text = "\n".join(dlls)
        tree.insert("", "end", values=(process, dll_text))

def get_loaded_dlls():
    loaded_dlls = {}
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_dlls = psutil.Process(process.info['pid']).memory_maps()
            dlls = [dll.path for dll in process_dlls if dll.path.lower().endswith('.dll')]
            loaded_dlls[process.info['pid']] = dlls
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    return loaded_dlls

def export_to_file(tree, file_prefix):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(f"{file_prefix}:\n\n")
                for item in tree.get_children():
                    values = tree.item(item, 'values')
                    file.write(f"Process ID: {values[0]}\n")
                    file.write(f"Loaded DLLs:\n{values[1]}\n\n")
            messagebox.showinfo("Export Successful", "Export to file was successful!")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting to file: {e}")

# if __name__ == "__main__":
#     run_list_loaded_dlls_tool()
