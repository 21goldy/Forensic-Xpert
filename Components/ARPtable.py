import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import subprocess
from StaticGUIConfigs import *


def run_arp_command():
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        return result.stdout.replace('\r\n', ' ')  # Replace newline characters with spaces
    except Exception as e:
        return f"Error running 'arp -a' command: {e}"


def export_to_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Export Successful", "Export to file was successful!")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting to file: {e}")


def analyzeARPtable(parent_window):
    result = run_arp_command()

    root = tk.Toplevel(parent_window)
    root.title("Analyze ARP Table")
    root.resizable(False, False)  # Disallow resizing of the mainWindow
    root['background'] = bgColor  # Set backgound color

    # Create a scrolled text widget with a fixed font
    output_text = scrolledtext.ScrolledText(
        root,
        height=20,
        width=60,  # Increase the width
        wrap=tk.WORD,
        background="lightblue",
        font=("Courier New", 10))  # Use a fixed-width font for better alignment
    output_text.pack(expand=True, fill="both")

    output_text.insert(tk.END, result)

    export_button = tk.Button(
        root,
        text="Export to File",
        command=lambda: export_to_file(output_text.get("1.0", tk.END)),
        background="darkgray",
        padx=10,
        pady=5)
    export_button.pack(pady=10)

    root.mainloop()

# if __name__ == "__main__":
#     run_arp_command_and_display()
