import tkinter as tk
from tkinter import ttk, filedialog
import winreg
from Components.StaticGUIConfigs import *

def usb_history_analyzer_tool(parent_window):
    def analyze_usb_history():
        key_path = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"
        
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                usb_devices = list(iter_subkeys(key))
                return usb_devices
        except Exception as e:
            return f"Error accessing registry: {e}"

    def iter_subkeys(key):
        i = 0
        while True:
            try:
                yield winreg.EnumKey(key, i)
                i += 1
            except OSError:
                break

    def show_output(message):
        usb_output.config(state=tk.NORMAL)  # Enable editing
        usb_output.delete("1.0", tk.END)  # Clear previous content
        usb_output.insert(tk.END, message)  # Insert new content
        usb_output.config(state=tk.DISABLED)  # Disable editing

    def export_to_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(usb_output.get("1.0", tk.END))

    root = tk.Toplevel(parent_window)
    root.title("USB History Analyzer")
    root.resizable(False, False) # Disallow resizing of the mainWindow
    root['background']=bgColor # Set backgound color

    style = ttk.Style()
    style.configure("TButton", padding=(10, 5, 10, 5), font=('Helvetica', 12))

    analyze_usb_button = ttk.Button(root, text="Analyze USB History", command=lambda: show_output("\n".join(analyze_usb_history())))
    analyze_usb_button.pack(pady=10)

    # Create a Text widget for the output
    usb_output = tk.Text(root, height=10, width=50, wrap="word")
    usb_output.pack(pady=10)

    # Button to export
    export_button = tk.Button(
        root,
        text="Export to File",
        command=export_to_file,
        background="darkgray",
        padx=10,
        pady=5)
    export_button.pack(pady=10)

    root.geometry("600x400")
    root.mainloop()

# if __name__ == "__main__":
#     usb_history_analyzer_tool() 
