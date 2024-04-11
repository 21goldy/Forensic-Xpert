import sqlite3
import os
import platform
import shutil
import pandas as pd
import tkinter
from tkinter import ttk
from StaticGUIConfigs import *
import CutPaste

def getChromeDownloads(parent_window):  # Accept the parent window as an argument

    # Detect the operating system to find the Chrome downloads history file location
    if platform.system() == 'Windows':
        downloads_file_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'History')
    elif platform.system() == 'Darwin':  # macOS
        downloads_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Google', 'Chrome', 'Default', 'History')
    elif platform.system() == 'Linux':
        downloads_file_path = os.path.join(os.path.expanduser('~'), '.config', 'google-chrome', 'Default', 'History')
    else:
        print("Unsupported operating system")
        return

    # Create a temporary copy of the downloads history file
    temp_copy_path = 'temp_downloads_copy'
    try:
        shutil.copy(downloads_file_path, temp_copy_path)
    except FileNotFoundError:
        print(f"Error: File not found - {downloads_file_path}")
        return

    # Connect to the Chrome downloads history SQLite database
    try:
        connection = sqlite3.connect(temp_copy_path)
        cursor = connection.cursor()

        # Execute a query to get the complete downloads history
        cursor.execute("SELECT id, target_path, total_bytes, received_bytes, start_time, end_time, state FROM downloads")
        rows = cursor.fetchall()  # Fetch all the rows

        # Create a Pandas DataFrame for better tabular formatting
        columns = ["ID", "Target Path", "Total Bytes", "Received Bytes", "Start Time", "End Time", "State"]
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv('chrome_downloads.csv', index=False)  # Save the DataFrame to a CSV file

    except sqlite3.Error as e:
        print(f"Error reading Chrome downloads history: {e}")

    finally: 
        if connection:
            connection.close()

        os.remove(temp_copy_path)  # Remove the temporary copy

    df = pd.read_csv('chrome_downloads.csv')  # Read the CSV file into a Pandas DataFrame

    # GUI
    downloadsWindow = tkinter.Toplevel(parent_window)  # Use Toplevel instead of Tk
    downloadsWindow.title("Google Chrome Downloads History")
    downloadsWindow.configure(background=bgColor)
    positionWindow(downloadsWindow, width=1000, height=730)

    titleText = tkinter.Label(downloadsWindow, text="ForensicXpert: Web Browser Forensics - Downloads History", bg="black", fg=pinkColor, pady=10, font=("Consolas", 15, "italic"))
    titleText.pack(side="top", fill="x")

    # Create a Treeview widget to display the CSV contents as a table
    style = ttk.Style()
    style.configure("Treeview",
                    background=bgColor,
                    fieldbackground=bgColor,
                    foreground="white",
                    font=("Consolas", 11))

    tree = ttk.Treeview(downloadsWindow, style="Treeview")
    tree["columns"] = ('Sr. No.',) + tuple(df.columns)

    # Configure columns
    for col in tree["columns"]:
        tree.column(col, anchor=tkinter.W)
        tree.heading(col, text=col)

    # Insert data into the Treeview with serial numbers
    for i, (index, row) in enumerate(df.iterrows(), start=0):
        tree.insert("", i, values=(str(i),) + tuple(row))

    # Set up vertical scrollbar
    yscrollbar = ttk.Scrollbar(downloadsWindow, orient="vertical", command=tree.yview)
    yscrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=yscrollbar.set)

    # Set up horizontal scrollbar
    xscrollbar = ttk.Scrollbar(downloadsWindow, orient="horizontal", command=tree.xview)
    xscrollbar.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=xscrollbar.set)

    tree.pack(expand=True, fill=tkinter.BOTH)  # Pack the Treeview
    downloadsWindow.mainloop()
    CutPaste.cut_and_paste_file("chrome_downloads.csv", "Evidence_Collection/chrome_downloads.csv") # Save history file to evidence
